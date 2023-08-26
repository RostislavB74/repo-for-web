import pickle


class ContactUid:
    def __init__(self):
        self.load_uid()  # Загрузка сохраненного значения uid
        self.value = self.generate_uid()
        self.save_uid()  # Сохранение нового значения uid

    def generate_uid(self):
        self.current_uid += 1
        return self.current_uid

    def save_uid(self):
        with open('uid.pickle', 'wb') as f:
            pickle.dump(self.current_uid, f)

    def load_uid(self):
        try:
            with open('uid.pickle', 'rb') as f:
                self.current_uid = pickle.load(f)
        except FileNotFoundError:
            self.current_uid = 0


if __name__ == "__main__":
    uid_instance = ContactUid()
    print(uid_instance.value)
