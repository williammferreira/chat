import json

from channels.generic.websocket import WebsocketConsumer

from django.core import serializers

from docs.models import Document, Group

class DocsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)

        id = text_data_json['id']
        
        document = Document.objects.filter(id=id)
        document_exists = document.exists()
        
        group = Group.objects.filter(id=id)
        group_exists = group.exists()
        
        if document_exists:
            self.send(text_data=json.dumps({
                'text': {
                    'title': document.title,
                    'body': document.body,
                }
            }))
            
        elif group_exists:
            singular_group = group[0]
            
            try:
                contained_groups = singular_group.group_children
                contained_docs = singular_group.document_children
            
                queryset = contained_groups | contained_docs
                
                json_queryset = serializers.serialize("json", queryset)
                
                self.send(text_data=json.dumps({
                    json_queryset
                }))
                
            except Exception:
                self.send(text_data=json.dumps({
                    'text': '',
                }))
                        
        else:
            self.send(text_data="")