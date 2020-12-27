class Storage:
    def __init__(self):
        self.categories: list = []
        self.topics: list = []
        self.documents: list = []

    def add_category(self, category):
        #  category: Category <- obj.
        if category not in self.categories:
            self.categories.append(category)

    def add_document(self, document):
        #  document: Document <- obj.
        if document not in self.documents:
            self.documents.append(document)

    def add_topic(self, topic):
        #  topic: Topic <- obj.
        if topic not in self.topics:
            self.topics.append(topic)

    def edit_category(self, category_id: int, new_name: str):
        self.get_category_by_id(category_id).edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.get_topic_obj_by_id(topic_id).edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.get_document_obj_by_id(document_id).edit(new_file_name)

    def delete_category(self, category_id):
        self.categories.remove(self.get_category_by_id(category_id))

    def delete_topic(self, topic_id):
        self.topics.remove(self.get_topic_obj_by_id(topic_id))

    def delete_document(self, document_id):
        self.documents.remove(self.get_document_obj_by_id(document_id))

    def get_document(self, document_id):
        return self.get_document_obj_by_id(document_id).__repr__()

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += doc.__repr__() + "\n"

        return result

    def get_category_by_id(self, category_id):
        category_obj = [category for category in self.categories if category.id == category_id][0]
        return category_obj

    def get_topic_obj_by_id(self, topic_id: int):
        topic_obj = [topic for topic in self.topics if topic.id == topic_id][0]
        return topic_obj

    def get_document_obj_by_id(self, document_id: int):
        document_obj = [document for document in self.documents if document.id == document_id][0]
        return document_obj


from document_managment.project.category import Category
from document_managment.project.document import Document
from document_managment.project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)

