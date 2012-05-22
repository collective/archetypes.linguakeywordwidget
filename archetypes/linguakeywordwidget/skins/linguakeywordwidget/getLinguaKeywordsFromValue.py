## Script (Python) "getlinguakeywordsvalue"
##title=Edit content
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=value

linguakeywords = []
language = context.Language()
for keyword in value:
    if keyword.startswith('%s-' % language):
        linguakeywords.append(keyword[len(language) + 1:])
    else:
        linguakeywords.append(keyword)

return linguakeywords
