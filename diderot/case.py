from assertion import Assertion
from unittest import TestCase

from diderot.utils import get_empty_graph


class DiderotTestCase(TestCase):
    """
        Diderot's main class. To use our framework your tests cases should extend this class.

        .. literalinclude :: ../../example/test/test_expected_facts.py
            :lines: 1-9

    """

    def __init__(self, *args, **kwargs):  # pragma: no cover
        super(DiderotTestCase, self).__init__(*args, **kwargs)

    def assertThat(self, assertion):
        """
            Function that uses a assertion object (``marvin.assertion.Assertion``) to check if the test will pass or not.

            Users should use this function instead of the usual ``assertEqual()`` or ``assertTrue()``
            from ``unittest.TestCase``.

            ``Assertion`` objects can be created by using utilitary functions such as ``can_infer()``.

            If the passed object is not an ``Assertion``, a ``RuntimeError`` is raised.
        """
        if isinstance(assertion, Assertion):
            if not assertion.assertion_value:
                ASSERTION_ERROR_MESSAGE = "Could not infer some expected facts:\n  {0}"
                not_inferred_graph = get_empty_graph()
                for triple in assertion.not_inferred_facts:
                    not_inferred_graph.add(triple)

                raise AssertionError(ASSERTION_ERROR_MESSAGE.format(not_inferred_graph.serialize(format="nt")))
        else:
            raise RuntimeError("The assertThat method expects an Assertion instance")
