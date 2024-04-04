from flask import Flask, redirect, render_template, request
from .filters import format_birthday, format_date

app = Flask(__name__)


app.add_template_filter(format_birthday)
app.add_template_filter(format_date)
