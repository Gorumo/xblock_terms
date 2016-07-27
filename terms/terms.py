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
    def termsListCheck(self, data, suffix=''):
        if self.exampleList != None:
            self.arr = json.loads(self.exampleList)

        new_term = data.get('term')
        new_id = data.get('id')

        cnx = mysql.connector.connect(**s.database)
        cursor = cnx.cursor()
        #try:
        cursor.execute("SELECT `id` FROM `allTerms` WHERE `name` = '"+new_term+"' ;")
        data = cursor.fetchall() 
        count = cursor.rowcount
        if count == 0:
            cursor.execute("INSERT INTO `allTerms` (`id`, `name`, `term`) VALUES (NULL, %s, %s)", (new_term, 'term_term'))
            count = cursor.lastrowid
            cnx.commit()
            cursor.execute("INSERT INTO `relations` (`id`, `block`, `term`) VALUES (NULL, %s, %s)", (new_id, count))
        else:
            term_id = data[0][0]
            cursor.execute("SELECT `id` FROM `relations` WHERE `term` = %s AND `block` = %s ;" % (term_id, new_id))
            cursor.fetchall()
            if cursor.rowcount == 0:
                cursor.execute("INSERT INTO `relations` (`id`, `block`, `term`) VALUES (NULL, %s, %s)", (new_id, term_id))
            else:
                new_id = 'Error'
                new_term = 'Error'
        cnx.commit()
        cursor.close() 
        cnx.close()
        #except mysql.connector.Error as err:
            #new_id = "Something went wrong: {}".format(err)
        return {"exampleList" : new_term ,"test" : new_id}

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
