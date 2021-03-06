"""TO-DO: Write a description of what this XBlock is."""
import json
import pkg_resources
import datetime
#import mysql.connector

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
#from mysql.connector import errorcode
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
import settings as s


class TermsXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.   
    #two arrays to store temp data

    arr = []
    overall = []

    exampleList = String(
        default=0, scope=Scope.settings,
        help="shows next nuber",
    )

    def resource_string(self, path): 
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    # TO-DO: change this view to display your data your own way.
    
    def student_view(self, context=None):
        """
        The primary view of the TermsXBlock, shown to students
        when viewing courses.
        """

        html = self.resource_string("static/html/terms.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/terms.css"))
        frag.add_javascript(self.resource_string("static/js/src/terms.js"))
        frag.initialize_js('TermsXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def termsListCheck(self, data, suffix=''):
        if self.exampleList != 0:
            self.arr = json.loads(self.exampleList)
        self.arr.append(data.get('term'))
        sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
        sparql.setQuery("""
            SELECT DISTINCT ?item ?itemLabel
			WHERE
			{
				?item wdt:P279* wd:Q24034552 .
			  	?item rdfs:label ?itemLabel
			  	FILTER regex(?itemLabel, "^multi", "i")
				SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }	
			}""")
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        
        for result in results["results"]["bindings"]:
            self.arr.append(result["item"]["value"])
            self.arr.append(result["itemLabel"]["value"])
        self.exampleList = json.dumps(self.arr) 
        return {"exampleList" : self.exampleList} 

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TermsXBlock",
             """<terms/>
             """),
            ("Multiple TermsXBlock",
             """<vertical_demo>
                <terms/>
                <terms/>
                <terms/>
                </vertical_demo>
             """),
        ]
