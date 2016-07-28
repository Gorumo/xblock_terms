"""TO-DO: Write a description of what this XBlock is."""
import json
import pkg_resources
import datetime
import mysql.connector

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from mysql.connector import errorcode
import settings as s


class TermsXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.  
    #big dick 
    
    arr = []
    overall = []

    exampleList = String(
        default=None, scope=Scope.settings,
        help="shows next nuber",
    )
    test = String(
        default=None, scope=Scope.settings,
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
    # than one handler, or you may not need any handlers at all. json.dumps
    @XBlock.json_handler
    def getTerms(self, data, suffix=''):
	    arr = [
            {"id" : 12, "phrase" : "Ball"},
            {"id" : 16,"phrase" : "Football"},
            {"id" : 17, "phrase" : "Softball"}
        ]
	    self.exampleList = json.dumps(arr)
	    return {"exampleList" : self.exampleList}
	    
    @XBlock.json_handler
    def termsListCheck(self, data, suffix=''):
        #Get data from html fields
        new_term = data.get('term')
        new_id = data.get('id') 
        field_id = 1
        cnx = mysql.connector.connect(**s.database)
        cursor = cnx.cursor()
        cursor.execute("SELECT `concept_id` FROM `Concepts` WHERE `concept_label` = '"+new_term+"' ;")
        data = cursor.fetchall() 
        count = cursor.rowcount
        if count == 0:
            cursor.execute("INSERT INTO `Concepts` (`concept_id`, `concept_URI`, `field_id`, `concept_label`, `concept_description`) VALUES (NULL, %s, %s, %s, %s)", ('URI', field_id, new_term,'Description of concept'))
            count = cursor.lastrowid
            cnx.commit()
            cursor.execute("INSERT INTO `Concept_Content_Manager` (`id_m`, `block_id`, `concept_id`) VALUES (NULL, %s, %s)", (new_id, count))
        else:
            term_id = data[0][0]
            cursor.execute("SELECT `id_m` FROM `Concept_Content_Manager` WHERE `concept_id` = %s AND `block_id` = %s ;" % (term_id, new_id))
            cursor.fetchall()
            if cursor.rowcount == 0:
                cursor.execute("INSERT INTO `Concept_Content_Manager` (`id_m`, `block_id`, `concept_id`) VALUES (NULL, %s, %s)", (new_id, term_id))
            else:
                new_id = 'Error'
                new_term = 'Error'
        cnx.commit()
        cursor.close() 
        cnx.close()
        self.exampleList = json.dumps(new_term)
        self.test = json.dumps(new_id)
        #except mysql.connector.Error as err:
        #new_id = "Something went wrong: {}".format(err)
        return {"exampleList" : self.exampleList ,"test" : self.test}

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
