# -*- coding: utf-8 -*-
import sys
import json
import codecs
import csv
from mismatch_case_precinct_map import mismatches

map_path = "../../kostat/"
map_filenames = {
	2012: {"provinces": "provinces-geo-simple.json", "municipalities": "municipalities-geo-simple.json", "submunicipalities": "submunicipalities-geo-simple.json"},
	2013: {"provinces": "skorea_provinces_geo_simple.json", "municipalities": "skorea_municipalities_geo_simple.json", "submunicipalities": "skorea_submunicipalities_geo_simple.json"}
}

# Load map files
def load_codes(year):
	# 지도 파일에서 시 정보가 미반영된 구 (e.g., 성산구 -> 창원시성산구)
	municipality_rename_add_city = mismatches["municipality_rename"][year]

	# Load map files
	with open(map_path+str(year)+"/json/"+map_filenames[year]["provinces"], "r") as f:
		provinces = [{"code": int(item["properties"]["code"]), "name": item["properties"]["name"]} for item in json.load(f)["features"]]
	with open(map_path+str(year)+"/json/"+map_filenames[year]["municipalities"], "r") as f:
		municipalities = [{"code": int(item["properties"]["code"]), "name": item["properties"]["name"], "province_name": [x["name"] for x in provinces if x["code"] == int(item["properties"]["code"])/1000][0]} for item in json.load(f)["features"]]
		for m in municipalities:
			if m["code"] in municipality_rename_add_city.keys():
				m["name"] = municipality_rename_add_city[m["code"]]
	with open(map_path+str(year)+"/json/"+map_filenames[year]["submunicipalities"], "r") as f:
		submunicipalities = [{"code": int(item["properties"]["code"]), "name": item["properties"]["name"]} for item in json.load(f)["features"]]
	
	print "%d, %d, %d" % (len(provinces), len(municipalities), len(submunicipalities))
	admin_districts = {"provinces": provinces, "municipalities": municipalities, "submunicipalities": submunicipalities}
	return admin_districts


# Load original precinct district table and create mappings to (sub)municipality codes in map files
def structure_precinct_table(assembly_no, districts):
	# 지도 파일 작성 시점과 선거구 획정 시점 사이에 읍면동 (submunicipality) 분할되거나 합쳐진 경우 등
	mismatch_changed = mismatches["submunicipality_changed"][assembly_no]
	# 새로 만들어진 시군구 (municipality)
	mismatch_new = mismatches["new_municipality"][assembly_no]

	province_code_map = dict([(item["name"], item["code"]) for item in districts["provinces"]])
	precincts = []
	province_code = -1
	province_name = u""
	precinct_no = 0
	
	with codecs.open("precinct_table_"+str(assembly_no)+".txt", "r", "UTF-8") as f:
		i = 0
		for line in f:
			i += 1
			if i > 2:
				# Determine line for province header
				if u"(지역구" in line[1:]:
					province_name = line[:line.index(u"(지역구")]
					province_code = province_code_map[province_name]
				
				# Determine line for each precinct
				elif "\t" in line and line.split("\t")[0].endswith(u"선거구"):
					precinct_no += 1
					precinct_name = line.split("\t")[0][:-3]

					precinct_m_name = precinct_name
					precinct_m_codes = []

					if precinct_name[-1] in [u"갑", u"을", u"병", u"정", u"무"]:
						# Find municipality code
						precinct_m_name = precinct_name[:-1]
						precinct_m_code_candidates = [muni for muni in districts["municipalities"] if muni["name"] == precinct_m_name and muni["code"]/1000 == province_code]
						if len(precinct_m_code_candidates) == 1:
							precinct_m_codes.append( precinct_m_code_candidates[0]["code"] )
						elif len(precinct_m_code_candidates) == 0:
							# for cases like 수원시팔달구
							precinct_m_code_candidates = [muni for muni in districts["municipalities"] if muni["name"].startswith(precinct_m_name) and muni["code"]/1000 == province_code]
							precinct_m_codes = [cand["code"] for cand in precinct_m_code_candidates]
							# for cases like 서구강화군갑
							if len(precinct_m_code_candidates) == 0:
								precinct_m_code_candidates = [muni for muni in districts["municipalities"] if precinct_m_name != muni["name"] and (precinct_m_name.startswith(muni["name"]) or precinct_m_name.endswith(muni["name"])) and muni["code"]/1000 == province_code]
								precinct_m_codes = [cand["code"] for cand in precinct_m_code_candidates]
							
					# List of municipalities or submunicipalities name
					item_list = line.split("\t")[1][:-3].split(", ")
					# List of municipalities or submunicipalities code
					code_list = []

					# 세종시
					if assembly_no in [19, 20] and precinct_name == u"세종특별자치시":
						item_list = [u"세종시 일원",]

					# 청주시
					if assembly_no in [19, 20] and precinct_name.replace(u" 일원", u"") in mismatch_new.keys():
						item_list = mismatch_new[precinct_name.replace(u" 일원", u"")]

					# Find code for each name
					for item in item_list:
						# Municipalities
						if u" 일원" in item:
							if "(" in item:
								item = item[:item.index("(")]
							m = item[:-3].replace(" ", "")
							cc = [muni for muni in districts["municipalities"] if muni["name"] == m and muni["code"]/1000 == province_code]
							if len(cc) >= 1:
								c = cc[0]
								code_list.append(c["code"])
								if len(cc) > 1:
									print precinct_no
									print "Need exception handling: add case to the separate exception case file" 
									code_list.append(-2)
							else:
								print precinct_no
								print "Need exception handling: add case to the separate exception case file" 
								code_list.append(-1)
						
						# Submunicipalities
						else:
							for k in range(1,10):
								item = item.replace(u"제"+str(k), str(k))
							if " " in item:
								m = item.split(" ")[0]
								# todo distmcode
								s = item.split(" ")[1]
							else:
								s = item
					
							# changed submunicipalities
							if len(precinct_m_codes) > 0:
								for precinct_m_code in precinct_m_codes:
									if (precinct_m_code, s) in mismatch_changed.keys():
										s = mismatch_changed[(precinct_m_code, s)]
										break
							
							if type(s) is list:
								# mismatch merged case
								cc = []
								for sx in s:
									cc += [subm for subm in districts["submunicipalities"] if subm["name"] == sx and subm["code"]/100 in precinct_m_codes and subm["code"]/100000 == province_code]
							elif len(precinct_m_codes) > 0:
								cc = [subm for subm in districts["submunicipalities"] if subm["name"] == s and subm["code"]/100 in precinct_m_codes and subm["code"]/100000 == province_code]
							else:
								cc = [subm for subm in districts["submunicipalities"] if subm["name"] == s and subm["code"]/100000 == province_code]

							if type(s) is list and len(cc) > 0:
								for c in cc:
									code_list.append(c["code"])

							elif len(cc) >= 1:
								c = cc[0]
								code_list.append(c["code"])
								if len(cc) > 1:
									print precinct_no
									print "Need exception handling: add case to the separate exception case file" 
									code_list.append(-2)
							else:
								print precinct_no
								print "Need exception handling: add case to the separate exception case file" 
								code_list.append(-1)

					precincts.append( {"no": precinct_no, "name": precinct_name, "province_code": province_code, "province": province_name, "list": item_list, "code_list": code_list} )
	
	d = {"precincts": precincts}
	with open("precinct_table_mapping_"+str(assembly_no)+".json", "w") as outfile:
		json.dump(d, outfile, indent=4)

	# Optional tsv file only for presentation
	with open("precinct_table_mapping_"+str(assembly_no)+".tsv", "w") as outfile:
		writer = csv.writer(outfile, precincts[0].keys(), delimiter='\t')
		for r in precincts:
			writer.writerow( (r["no"], r["name"].encode('utf-8'), r["province_code"], r["province"].encode('utf-8'), ";".join(r["list"]).encode('utf-8'), ";".join([str(c) for c in r["code_list"]]) ) )

	print "Done creating mapping file"


# Modify submunicipality map file to add precinct no: 
# for each submunicipality, add a property for precinct no to be used for merging submunicipalities in the same precinct
def update_geo_file(assembly_no):
	file_name = {
		19: "../../kostat/2012/json/submunicipalities-topo.json",
		20: "../../kostat/2013/json/skorea_submunicipalities_topo.json",
	}

	district_to_precinct = {}
	with open("precinct_table_mapping_"+str(assembly_no)+".json", "r") as f:
		precincts = json.load(f)["precincts"]
		for p in precincts:
			for c in p["code_list"]:
				if c in district_to_precinct.keys(): 
					print "Already exist "+str(c)+": could be fine because it is from splitted districts"
				district_to_precinct[int(c)] = (int(p["no"]), p["name"], p["province"]) 
	
	with open(file_name[assembly_no], "r") as f:
		d = json.load(f)

	d["objects"]["precincts"] = d["objects"].pop(dict.keys(d["objects"])[0])
	
	for s in d["objects"]["precincts"]["geometries"]:
		code = int(s["properties"]["code"])
		if code in district_to_precinct.keys():
			s["properties"][u"precinct_no"] = str(district_to_precinct[code][0])
			s["properties"][u"precinct_name"] = district_to_precinct[code][1]
			s["properties"][u"province"] = district_to_precinct[code][2]
		elif code/100 in district_to_precinct.keys():
			s["properties"][u"precinct_no"] = str(district_to_precinct[code/100][0])
			s["properties"][u"precinct_name"] = district_to_precinct[code/100][1]
			s["properties"][u"province"] = district_to_precinct[code/100][2]
		else:
			print "Does not have precinct no: may need exception handling"
			print code
	
	with open("merge_ready_submunicipalities_into_precinct_"+str(assembly_no)+".json", "w") as outfile:
		json.dump(d, outfile, indent=4)

	print "Done modifying map file"
	print "The next step is to perform the mapshaper's dissolve function to merge submunicipalities in the same precinct:"
	print "mapshaper merge_ready_submunicipalities_into_precinct_"+str(assembly_no)+".json -dissolve precinct_no copy-fields=precinct_name,province -o assembly-precinct-"+str(assembly_no)+"-geo.json"

if __name__ == "__main__":
	# 19th assembly precinct to kostat 2012 map
	admin_districts = load_codes(2012)
	structure_precinct_table(19, admin_districts)
	update_geo_file(19)

	# 20th assembly precinct to kostat 2013 map
	admin_districts = load_codes(2013)
	structure_precinct_table(20, admin_districts)
	update_geo_file(20)
	