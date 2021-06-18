#! /usr/bin/python3
import news2line_line
import news2line_feed

text = news2line_feed.feed('https://karapaia.com/index.rdf')
news2line_line.line_send(text)
