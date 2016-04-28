"""TO-DO: Write a description of what this XBlock is."""
import json
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment




class TermsXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """
    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.   

    arr = []

    exampleList = String(
        default=0, scope=Scope.user_state,
        help="shows next nuber",
    )

    conceptsSet = String(
        default=0, scope=Scope.user_state_summary,
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
        if self.conceptsSet != 0:
            self.arr = json.loads(self.conceptsSet)
        self.arr.append(data.get('term'))

        self.conceptsSet = json.dumps(self.arr)
        self.exampleList = self.conceptsSet

        return {"exampleList" : self.exampleList, "conceptsSet" : self.conceptsSet}

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
