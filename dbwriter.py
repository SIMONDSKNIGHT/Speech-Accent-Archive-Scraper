import pandas as pd

class DBWriter:
    def __init__(self):
        self.data = {
            'identifier': [], 
            'birth_place': [],
            'native_language': [],
            'other_languages': [],
            'age': [],
            'sex': [],
            'age_of_english_onset': [],
            'english_learning_method': [],
            'english_residence': [],
            'length_of_english_residence': [],
            'mp3_name': []
        }
    
    def add_entry(self,identifier, birth_place, native_language, other_languages, age, sex, age_of_english_onset, english_learning_method, english_residence, length_of_english_residence, mp3_name):
        self.data['identifier'].append(identifier)
        self.data['birth_place'].append(birth_place)
        self.data['native_language'].append(native_language)
        self.data['other_languages'].append(other_languages)
        self.data['age'].append(age)
        self.data['sex'].append(sex)
        self.data['age_of_english_onset'].append(age_of_english_onset)
        self.data['english_learning_method'].append(english_learning_method)
        self.data['english_residence'].append(english_residence)
        self.data['length_of_english_residence'].append(length_of_english_residence)
        self.data['mp3_name'].append(mp3_name)
    
    def create_database(self, filename):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
    def read_from_csv(self, filename):
        df = pd.read_csv(filename)
        self.data = df.to_dict(orient='list')

        
    def unique_identifier(self, identifier):
        if identifier in self.data['identifier']:
            return False
        else:
            return True
