#!/usr/bin/python
"""Hyperion Constants."""

KEY_ACCEPT = "accept"
KEY_ADJUSTMENT = "adjustment"
KEY_AUTHORIZE = "authorize"
KEY_AUTHORIZE_LOGIN = "authorize-login"
KEY_AUTHORIZE_LOGOUT = "authorize-logout"
KEY_BRIGHTNESS = "brightness"
KEY_CLEAR = "clear"
KEY_CLIENT = "client"
KEY_COLOR = "color"
KEY_COMMAND = "command"
KEY_COMPONENT = "component"
KEY_COMPONENTSTATE = "componentstate"
KEY_COMPONENTS = "components"
KEY_CONNECTION = "connection"
KEY_CONNECTED = "connected"
KEY_DATA = "data"
KEY_EFFECT = "effect"
KEY_EFFECTS = "effects"
KEY_ENABLED = "enabled"
KEY_LED_MAPPING = "imageToLedMapping"
KEY_LED_MAPPING_TYPE = "imageToLedMappingType"
KEY_ID = "id"
KEY_IMAGE = "image"
KEY_IMAGE_STREAM_START = "imagestream-start"
KEY_IMAGE_STREAM_STOP = "imagestream-stop"
KEY_INFO = "info"
KEY_INSTANCE = "instance"
KEY_LEDCOLORS = "ledcolors"
KEY_LED_STREAM_START = "ledstream-start"
KEY_LED_STREAM_STOP = "ledstream-stop"
KEY_LEDS = "leds"
KEY_LED_MAPPING = "imageToLedMapping"
KEY_LOADED_STATE = "loaded-state"
KEY_LOGGED_IN = "logged-in"
KEY_LOGIN = "login"
KEY_LOGOUT = "logout"
KEY_NAME = "name"
KEY_ORIGIN = "origin"
KEY_OWNER = "owner"
KEY_PRIORITY = "priority"
KEY_PRIORITIES = "priorities"
KEY_PRIORITIES_AUTOSELECT = "priorities_autoselect"
KEY_PROCESSING = "processing"
KEY_RGB = "RGB"
KEY_REQUIRED = "required"
KEY_REQUEST_TOKEN = "requestToken"
KEY_RUNNING = "running"
KEY_SESSIONS = "sessions"
KEY_SET_VIDEOMODE = "videoMode"
KEY_SERVERINFO = "serverinfo"
KEY_SOURCESELECT = "sourceselect"
KEY_START_INSTANCE = "startInstance"
KEY_STATE_LOADED = "startInstance"
KEY_STOP_INSTANCE = "stopInstance"
KEY_SUBCOMMAND = "subcommand"
KEY_SUBSCRIBE = "subscribe"
KEY_SUCCESS = "success"
KEY_SWITCH_TO = "switchTo"
KEY_STATE = "state"
KEY_TAN = "tan"
KEY_TIMEOUT_SECS = "timeout_secs"
KEY_TOKEN = "token"
KEY_TOKEN_REQUIRED = "tokenRequired"
KEY_UPDATE = "update"
KEY_VALUE = "value"
KEY_VIDEOMODE = "videomode"
KEY_VISIBLE = "visible"
KEY_VIDEOMODES = ["2D", "3DSBS", "3DTAB"]

# ComponentIDs from: https://docs.hyperion-project.org/en/json/Control.html#components-ids-explained
KEY_COMPONENTID = "componentId"
KEY_COMPONENTID_ALL = "ALL"
KEY_COMPONENTID_COLOR = "COLOR"
KEY_COMPONENTID_EFFECT = "EFFECT"

KEY_COMPONENTID_SMOOTHING = "SMOOTHING"
KEY_COMPONENTID_BLACKBORDER = "BLACKBORDER"
KEY_COMPONENTID_FORWARDER = "FORWARDER"
KEY_COMPONENTID_BOBLIGHTSERVER = "BOBLIGHTSERVER"
KEY_COMPONENTID_GRABBER = "GRABBER"
KEY_COMPONENTID_LEDDEVICE = "LEDDEVICE"
KEY_COMPONENTID_V4L = "V4L"

KEY_COMPONENTID_EXTERNAL_SOURCES = [
    KEY_COMPONENTID_BOBLIGHTSERVER,
    KEY_COMPONENTID_GRABBER,
    KEY_COMPONENTID_V4L,
]

DEFAULT_INSTANCE = 0
DEFAULT_CONNECTION_RETRY_DELAY_SECS = 30
DEFAULT_TIMEOUT_SECS = 5
DEFAULT_REQUEST_TOKEN_TIMEOUT_SECS = 180
DEFAULT_ORIGIN = "hyperion-py"
DEFAULT_PORT = 19444
