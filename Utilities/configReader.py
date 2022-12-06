from configparser import ConfigParser
import os

class ConfigReader():
    parser = None
    def __init__(self,fileName):
        ConfigReader.parser=ConfigParser()
        ConfigReader.parser.read(fileName)
        self.fileName=fileName
        
        
    def get_all_sections(self):
        return self.parser.sections()
    
    def get_all_options_in_a_section(self,section):
        return self.parser.options(section)
    def get_data_from_a_section(self,section,attribute):
        return ConfigReader.parser.get(section,attribute)

    def is_section_file(self,section):
        return section in self.parser
    def create_section(self,section):
        return self.parser.set(section)
    def update_attribute_section(self,section,key,value):
        return self.parser.set(section,key,value)
    def update_and_save_attribute_section(self,section,key,value,fileName=None):
        self.parser.set(section,key,value)
        if fileName is None:
            fileName=self.fileName
            
        self.write_to_file(fileName)
    def write_to_file(self,section=None,dict_data=None, fileName=None):
        
        if dict_data is not None:
            self.parser[section]=dict_data
        if fileName==None:
            fileName=self.fileName
        with open(fileName,'w') as file:
            self.parser.write(file)
    def get_attributes_of_screen(self,screen):
        dict_screen_details = {}
        for data in self.get_all_sections():

            section = data.split("_")

            if section[0].lower() == screen.strip().lower():

                li_attributes = []
                for data2 in self.get_all_options_in_a_section(data):
                    attributes = self.get_data_from_a_section(data, data2)
                    li_attributes.append(attributes)
                dict_screen_details["_".join(section[1:])] = li_attributes
        return dict_screen_details
#config=ConfigReader("C:\\Users\\028906744\\Documents\\selenium\\Odd Logic\\Config Files\\configuration.ini")
#print(config.get_all_sections())

#print(config.get_attributes_of_screen("Welcome to the Test Site "))
#     print(config.get_all_options_in_a_section(data))
 #    for data2 in config.get_all_options_in_a_section(data):
        
  #       print(config.get_data_from_a_section(data,data2))

#     print("========================")
# section="Text"
# dict_data={}
# dict_data["Name"]="Jinu"
# dict_data["Title"]="Nayak"
# config.update_and_save_attribute_section(section,"name","Jinu")
