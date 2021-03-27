from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def get_obj_from_id(obj_id, obj_list):
        obj = [o for o in obj_list if o.id == obj_id]
        if obj:
            return obj[0]

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_obj = self.get_obj_from_id(category_id, self.categories)
        category_obj.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic_obj = self.get_obj_from_id(topic_id, self.topics)
        topic_obj.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document_obj = self.get_obj_from_id(document_id, self.documents)
        document_obj.edit(new_file_name)

    def delete_category(self, category_id):
        category_obj = self.get_obj_from_id(category_id, self.categories)
        self.categories.remove(category_obj)

    def delete_topic(self, topic_id):
        topic_obj = self.get_obj_from_id(topic_id, self.topics)
        self.topics.remove(topic_obj)

    def delete_document(self, document_id):
        document_obj = self.get_obj_from_id(document_id, self.documents)
        self.documents.remove(document_obj)

    def get_document(self, document_id):
        doc_obj = self.get_obj_from_id(document_id, self.documents)
        return str(doc_obj)

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)