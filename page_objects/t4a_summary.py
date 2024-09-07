from page_objects.common_objects import CommonObjects


class T4ASummary(CommonObjects):
	t4a_summary_xpaths = {
		"saveButton": "//button[contains(text(),'Save')]",
		"transmitterAlertRequired":
			"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
			"/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]"
			"/div[1]/div[32]/div[2]/div[1]/div[2]/span[1]/span[1]",
		"issuerAlertRequired":
			"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
			"/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]"
			"/div[1]/div[32]/div[2]/div[4]/div[2]/span[1]/span[1]",
		"contactRequiredAlert":
			"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
			"/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]"
			"/div[32]/div[2]/div[7]/div[3]/span[1]/span[1]",
		"accountNumber": "//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div/div/div[4]/input",
		"clientName": "//*[@class='mb-5 mt-5 pt-2 font-weight-bold text-dark form-group']",
		"companyAddressInfo": "//*[@class='pt-2 form-group']",
		"totalNumberOfT4a":
			"//*[@id='inspire']/div/main/div/div/div[2]/span"
			"/form/div[2]/div/div/div/div[8]/div[3]/input",
		"pensionOrSuperannuation":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[9]/div[3]/input",
		"lumpSumPayments":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[10]/div[3]/input",
		"selfEmployedCommissions":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[11]/div[3]/input",
		"annuities":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[12]/div[3]/input",
		"otherIncome":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[13]/div[3]/input",
		"patronageAllocations":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[14]/div[3]/input",
		"rppContributions":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[15]/div[3]/input",
		"pensionAdjustment":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[16]/div[3]/input",
		"respAccumulatedIncomePayments":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[17]/div[3]/input",
		"respEducationalAssistancePayments":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[18]/div[3]/input",
		"fees":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[19]/div[3]/input",
		"otherInformation":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[20]/div[3]/input",
		"totalIncomeTaxDeducted":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[21]/div[3]/input",
		"remittance":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[22]/div[3]/input",
		"difference":
			"//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[24]/div[3]/input",
		"overpayment":
			"//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[26]/div[3]/input",
		"balanceDue":
			"//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[27]/div[3]/input",
		"RegistrationNumbersForRppOrDpsp071":
			"//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[29]/div[3]/input",
		"RegistrationNumbersForRppOrDpsp072":
			"//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[30]/div[3]/input",
		"RegistrationNumbersForRppOrDpsp073":
			"//*[@id='inspire']/div[1]/main/div/div/div[2]/span/form"
			"/div[2]/div/div/div/div[31]/div[3]/input",
		"transmitter":
			"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
			"/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]"
			"/div[32]/div[2]/div[1]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input",
		"xmlType":
			"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
			"/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]"
			"/div[32]/div[2]/div[2]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input",
		"issuer":
			"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
			"/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]"
			"/div[32]/div[2]/div[4]/div[2]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input",
		"sin1":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form/"
			"div[2]/div/div/div/div[32]/div[2]/div[5]/div[3]/input",
		"sin2":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form/"
			"div[2]/div/div/div/div[32]/div[2]/div[6]/div[3]/input",
		"contactPerson":
			"//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]"
			"/main[1]/div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]"
			"/div[32]/div[2]/div[7]/div[3]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input",
		"areaCode":
			"//*[@id='inspire']/div/main/div/div/div[2]/span/form/div[2]/div/div/"
			"div/div[32]/div[2]/div[9]/div[3]/input",
		"telephoneNum": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[9]/div[4]/input",
		"ext": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[9]/div[5]/input",
		"toastMessage": "//div[@class='toast-body']",
		"closeToast": "//button[contains(text(),'×')]",
		"generateXmlButton": "//button[contains(text(),'Generate XML')]",
		"printButton": "//button[contains(text(),'Print')]",
		"invoiceModal": "//div[@id='invoice_modal___BV_modal_content_']"
		
	}
