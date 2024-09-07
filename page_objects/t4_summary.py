from page_objects.common_objects import CommonObjects


class T4Summary(CommonObjects):
    """This class contains webElements of t4 summary page"""
    t4_summary_xpaths = {
        "saveButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                      "/div[2]/span[1]/form[1]/div[1]/div[1]/button[1]",
        "confirmationNo": "//input[@placeholder = 'Confirmation No.']",
        "deleteConfirmationButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/"
                                    "div[1]/div[1]/div[2]/span[1]/form[1]/div[1]/div[1]/button[2]",
        "generateXml": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/"
                       "div[2]/span[1]/form[1]/div[1]/div[1]/button[3]",
        "generateXmlDisabled": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]"
                               "/div[1]/div[2]/span[1]/form[1]/div[1]/div[1]/button[4]",
        "printButton": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                       "/div[2]/span[1]/form[1]/div[1]/div[1]/button[2]",
        "employersAccNo": "//*[@class='summary_business_no_field form-control']",
        "companyName": "//*[@class='mb-5 mt-5 pt-2 font-weight-bold text-dark form-group']",
        "addressInfo": "//*[@class='pt-2 form-group']",
        "noOfSlips": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[8]/div[3]/input",
        "employmentIncome": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[9]/div[3]/input",
        "rpp": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[10]/div[3]/input",
        "pensionAdjustment": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[11]/div[3]/input",
        "employeesCpp": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[13]/div[3]/input",
        "employersCpp": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[14]/div[3]/input",
        "employeesEi": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[15]/div[3]/input",
        "employersEi": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[16]/div[3]/input",
        "incomeTaxDeducted": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[17]/div[3]/input",
        "totalDeductionReport": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[18]/div[3]/input",
        "minusRemittance": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[19]/div[3]/input",
        "difference": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[21]/div[3]/input",
        "overPayment": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[23]/div[3]/input",
        "balanceDue": "//*[contains(@class, 'col-xl-8 offset-xl-2')]/div[24]/div[3]/input",
        "transmitter": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/di"
                       "v[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[1]/div[2]/span[1]/div[1]"
                       "/div[1]/div[1]/div[1]/div[1]/input",
        "xmlType": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/div"
                   "[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[2]/div[2]/span[1]/div[1]/div"
                   "[1]/div[1]/div[1]/div[1]/input",
        "notes": "//textarea",
        "issuer": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]/div[2]"
                  "/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[4]/div[2]/span[1]/div[1]/div[1]/div"
                  "[1]/div[1]/div[1]/input",
        "sin1OfProprietor": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[5]/div[3]/input",
        "sin2OfProprietor": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[6]/div[3]/input",
        "contactPerson": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/div[1]/div[1]"
                         "/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/div[7]/div[3]/span[1]/div"
                         "[1]/div[1]/div[1]/div[1]/div[1]/input",
        "areaCode": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[9]/div[3]/input",
        "telephoneNo": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[9]/div[4]/input",
        "ext": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[9]/div[5]/input",
        "transmitterRequiredAlert": "//body/div[@id='__nuxt']/div[@id='__layout']/div[@id='inspire']/div[1]/main[1]/"
                                    "div[1]/div[1]/div[2]/span[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[25]/div[2]/"
                                    "div[1]/div[2]/span[1]/span[1]",
        "issuerRequiredAlert": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[4]/div[2]/span[1]/span[1]",
        "contactPersonRequiredAlert": "//*[contains(@class, 'v-card__text pl-7 pr-7')]/div[7]/div[3]/span[1]/span[1]",
        "toastMessage": "//div[@class='toast-body']",
        "toastTitle": "//strong[contains(text(),'Success')]",
        "closeToast": "//button[contains(text(),'×')]",
        "invoiceModal": "//div[@id='invoice_modal___BV_modal_content_']"

    }
