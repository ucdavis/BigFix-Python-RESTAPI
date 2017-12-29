import requests
import requests.packages.urllib3
from BigFix import errors

class BigFix(object):
    '''
    Used to interact with the BigFix API
    '''
    requests.packages.urllib3.disable_warnings()

    def __init__(self,url,login,password, session=None):
        self.url = url
        self.login = login
        self.password =  password
        self.session = requests.Session()
        #self.authenticate()

    def get(self, apicall, params=None):
        '''
        Issues a get call to the bigfix api
        '''
        r = self.session.get(self.url + apicall, auth=(self.login,
                    self.password), verify=False, params=params)
        self.check_response(r.status_code)
        return r.text

    def post(self, apicall, params=None, data=None):
        '''
        Post to BigFix WebAPI
        '''
        r = self.session.post(self.url + apicall, auth=(self.login,
                    self.password), verify=False, params=params, data=data)
        self.check_response(r.status_code)
        return r.text

    def delete(self, apicall, params=None):
        '''
        Delete to BigFix WebAPI
        '''
        r = self.session.delete(self.url + apicall, auth=(self.login,
                    self.password), verify=False, params=params)
        self.check_response(r.status_code)
        return r.text

    def authenticate(self):
        ''' Authenticate to the BigFix API'''
        r = self.get('login')

    def check_response(self, response_code):
        ''' Checks the value of the response code from a requests call'''
        self.response_code = response_code
        if response_code == 200:
            pass
        else:
            raise ResponseError('Response code of ' + str(response_code) + ' returned'
                             ' expected 200' )

    def singleaction_xml(computer_id, action_title, actionscript, relevance ):
        self.action_title = action_title
        self.computer_id =  computer_id
        self.actionscript = actionscript
        self.relevance = relevance

        elem = etree.Element('BES')
        action = etree.SubElement(elem, 'SingleAction')
        action_title = etree.SubElement(action, 'Title')
        action_title.text = self.action_title
        action_relevance = etree.SubElement(action, 'Relevance')
        action_relevance.text = self.relevance
        action_actionscript = etree.SubElement(action, 'ActionScript',
                                                   MIMEType="application/x-Fixlet-Windows-Shell")
        action_actionscript = self.actionscript
        action_settings = etree.SubElement(action, 'Settings')
        action_enddate = etree.SubElement(action_settings, 'EndDateTimeLocalOffset')
        action_enddate.text = 'P1D'
        action_target = etree.SubElement(action, 'Target')
        action_target_id = etree.SubElement(action_target, 'ComputerID')
        action_target_id.text = computer_id
        xml = etree.tostring(elem, pretty_print=True, xml_declaration=True,
                                 encoding="UTF-8")
        return settings_xml
        
        




