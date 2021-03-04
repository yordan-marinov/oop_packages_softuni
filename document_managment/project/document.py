class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id: int = id
        self.category_id: int = category_id
        self.topic_id: int = topic_id
        self.file_name: str = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id: int, category, topic, file_name: str):
        # category: Category, topic: Topic <- this are objects.
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name: str = file_name

    def __repr__(self):
        return (
            f"Document {self.id}: {self.file_name}; "
            f"category {self.category_id}, topic {self.topic_id}, "
            f"tags: {', '.join(self.tags)}"
        )
