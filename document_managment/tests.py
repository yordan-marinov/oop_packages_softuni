from unittest import TestCase, main

from project.topic import Topic
from project.category import Category
from project.document import Document 
from project.storage import Storage 


class DocumentManagmentTests(TestCase):
    def setUp(self):
        self.topic = Topic(1, "topic", "documets")
        self.category = Category(1, "work")
        self.document = Document(1, 1, 1, "document file name")
        
    def test_topic_init(self):
        self.assertEqual(1, self.topic.id)
        self.assertEqual("topic", self.topic.topic)
        self.assertEqual("documets", self.topic.storage_folder)

    def test_edit_topic_to_change_new_topic_and_new_storage_folder(self):
        self.topic.edit("new topic", "new documets")
        self.assertEqual("new topic", self.topic.topic)
        self.assertEqual("new documets", self.topic.storage_folder)

    def test_topic_repr_correct_output(self):
        expected = "Topic 1: topic in documets"
        self.assertEqual(expected, str(self.topic))
        
    def test_category_init(self):
        self.assertEqual(1, self.category.id)
        self.assertEqual("work", self.category.name)

    def test_edit_category_to_change_new_topic_and_new_storage_folder(self):
        self.category.edit("new name")
        self.assertEqual("new name", self.category.name)

    def test_category_repr_correct_output(self):
        self.assertEqual("Category 1: work", str(self.category))
    
    def test_document_init(self):
        self.assertEqual(1, self.document.id)
        self.assertEqual(1, self.document.category_id)
        self.assertEqual(1, self.document.topic_id)
        self.assertEqual("document file name", self.document.file_name)

    def test_document_correct_inicialization_from_instance(self):
        self.doc1 = self.document.from_instances(2, self.category, self.topic, "file")
        self.assertEqual(2, self.doc1.id)
        self.assertEqual(1, self.doc1.category_id)
        self.assertEqual(1, self.doc1.topic_id)
        self.assertEqual("file", self.doc1.file_name)
        
    def test_document_add_tag_if_append_str_which_are_not_in_cls_tags(self):
        self.document.add_tag("Hello")
        self.assertIn("Hello", self.document.tags)

    def test_document_add_tag_if_not_append_str_which_are_in_cls_tags(self):
        self.document.add_tag("Hello")
        self.document.add_tag("Hello")
        self.assertEqual(["Hello"], self.document.tags)
        
    def test_document_repr_correct_output(self):
        self.document.add_tag("Hello")
        self.document.add_tag("World")
        expected = "Document 1: document file name; category 1, topic 1, tags: Hello, World"
        self.assertEqual(expected, str(self.document))

    def test_document_remove_tag_if_tag_in_cls_tags(self):
        self.document.add_tag("Hello")
        self.document.remove_tag("Hello")
        self.assertNotIn("Hello", self.document.tags)
        
    def test_documet_edit_to_change_file_name_to_new_file_name(self):
        self.document.edit("new file name")
        self.assertEqual("new file name", self.document.file_name)

    
    
if __name__ == "__main__":
    main()
