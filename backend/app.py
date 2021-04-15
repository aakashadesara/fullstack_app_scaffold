# to run:
# python app.py runserver 

import os
import sys
import json
from dataclasses import dataclass
from db import store, retrieve

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import path
from django.utils.crypto import get_random_string

settings.configure(
    DEBUG=True,
    ALLOWED_HOSTS=["*"],  # Disable host header validation
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY=get_random_string(
        50
    ),  # We aren't using any security features but Django requires this setting
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
        "middleware.CORSMiddleware.CORSMiddleware"
    ],
)

@dataclass
class Node:
    def __init__(self, val) -> None:
        self.val = val

    def as_dict(self) -> dict:
        return {
            "val": self.val,
        }

# Replace all instances of 
#       ``` nodes = retrieve('nodes') or [] ```
# with
#       ``` global nodes ```
# to use this array instead of db
nodes = [
    Node("aakash").as_dict(),
    Node("adesara").as_dict(),
]

def index(request):
    return HttpResponseRedirect("/nodes/")

def nodes_list(request):
    
    nodes = retrieve('nodes') or []
    return JsonResponse(
        {"data": [node for node in nodes]}
    )

def nodes_detail(request, node_id):
    
    nodes = retrieve('nodes') or []
    try:
        node = nodes[node_id]
    except KeyError:
        return JsonResponse(
            status=404,
            data={"error": f"Character with id {node_id!r} does not exist."},
        )
    return JsonResponse({"data": node})

def node_search(request):
    
    nodes = retrieve('nodes') or []
    query_val = request.GET.get('val')

    filtered_nodes = []
    for node in nodes:
        if (query_val in node['val']):
            filtered_nodes.append(node)

    return JsonResponse({'data': filtered_nodes})

def add_node(request):
    
    nodes = retrieve('nodes') or []
    body = json.loads(request.body)

    val = body['val']
    node = Node(val)
    nodes += [node.as_dict()]

    store('nodes', nodes)

    return JsonResponse({
        'data': node.as_dict()
    })

urlpatterns = [
    path("", index),
    path("nodes/", nodes_list),
    path("nodes/<int:node_id>/", nodes_detail),
    path("search/", node_search),
    path("addnode/", add_node),
]

app = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)