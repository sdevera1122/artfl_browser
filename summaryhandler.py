import json
def getVCFSummary():
	with open("variant_effect_output.txt_summary.txt") as ff:
		flag_vc = False
		flag_cms = False
		flag_ca = False
		flag_cc = False
		flag_ss = False
		flag_ps = False
		flag_vbyc = False

		variant_classes = {}
		consequences_ms = {}
		consequences_all = {}
		coding_consequences = {}
		sift_summary = {}
		polyphen_summary = {}
		variants_by_chromosome = {}
		
		mydata = ff.readlines()
		for row in mydata:
			currline = row.strip()
			if currline == '[Variant classes]':
				flag_vc = True
				flag_cms = False
				flag_ca = False
				flag_cc = False
				flag_ss = False
				flag_ps = False
				flag_vbyc = False
				continue
			elif currline == '[Consequences (most severe)]':
				flag_cms = True
				flag_vc = False
				flag_ca = False
				flag_cc = False
				flag_ss = False
				flag_ps = False
				flag_vbyc = False
				continue
			elif currline == '[Consequences (all)]':
				flag_ca = True
				flag_cms = False
				flag_vc = False
				flag_cc = False
				flag_ss = False
				flag_ps = False
				flag_vbyc = False
				continue
			elif currline == '[Coding consequences]':
				flag_cc = True
				flag_ca = False
				flag_cms = False
				flag_vc = False
				flag_ss = False
				flag_ps = False
				flag_vbyc = False
				continue
			elif currline == '[SIFT summary]':
				flag_ss = True
				flag_cc = False
				flag_ca = False
				flag_cms = False
				flag_vc = False
				flag_ps = False
				flag_vbyc = False
				continue
			elif currline == '[PolyPhen summary]':
				flag_ps = True
				flag_ss = False
				flag_cc = False
				flag_ca = False
				flag_cms = False
				flag_vc = False
				flag_vbyc = False
				continue
			elif currline == '[Variants by chromosome]':
				flag_vbyc = True
				flag_ps = False
				flag_ss = False
				flag_cc = False
				flag_ca = False
				flag_cms = False
				flag_vc = False
				continue
			elif currline == '':
				flag_ps = False
				flag_ss = False
				flag_cc = False
				flag_ca = False
				flag_cms = False
				flag_vc = False
				flag_vbyc = False

			if flag_vc == True:
				if currline != '':
					tmpVC = currline.split("\t")
					variant_classes[tmpVC[0]] = tmpVC[1]
			if flag_cms == True:
				if currline != '':
					tmpCMS = currline.split("\t")
					consequences_ms[tmpCMS[0]] = tmpCMS[1]
			if flag_ca == True:
				if currline != '':
					tmpCA = currline.split("\t")
					consequences_all[tmpCA[0]] = tmpCA[1]
			if flag_cc == True:
				if currline != '':
					tmpCC = currline.split("\t")
					coding_consequences[tmpCC[0]] = tmpCC[1]
			if flag_ss == True:
				if currline != '':
					tmpSS = currline.split("\t")
					sift_summary[tmpSS[0]] = tmpSS[1]
			if flag_ps == True:
				if currline != '':
					tmpPS = currline.split("\t")
					polyphen_summary[tmpPS[0]] = tmpPS[1]
			if flag_vbyc == True:
				if currline != '':
					tmpVbyC = currline.split("\t")
					variants_by_chromosome[tmpVbyC[0]] = tmpVbyC[1]

		#print variant_classes,consequences_ms,consequences_all
		summaryDict = {}
		summaryDict['variant_classes'] = variant_classes
		summaryDict['consequences_ms'] = consequences_ms
		summaryDict['consequences_all'] = consequences_all
		summaryDict['coding_consequences'] = coding_consequences
		summaryDict['sift_summary'] = sift_summary
		summaryDict['polyphen_summary'] = polyphen_summary
		summaryDict['variants_by_chromosome'] = variants_by_chromosome
		#print summaryDict
		return summaryDict

#getVCFSummary()
