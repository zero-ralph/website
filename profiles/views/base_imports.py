from django.contrib import messages
from django.shortcuts import (
    render,
    reverse,
    redirect, 
    get_object_or_404
)

from ..forms import *
# common
from common.views import *