
"""
This contains a simple view for rendering the webclient
page and serve it eventual static content.

"""
from __future__ import print_function
from django.shortcuts import render
from django.contrib.auth import login, authenticate

from evennia.accounts.models import AccountDB
from evennia.utils import logger


def webclient(request):
    """
    Webclient page template loading.

    """
    # auto-login is now handled by evennia.web.utils.middleware
    
    # make sure to store the browser session's hash so the webclient can get to it!
    pagevars = {'browser_sessid': request.session.session_key}

    return render(request, 'webclient.html', pagevars)
