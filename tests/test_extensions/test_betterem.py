"""Test cases for BetterEm."""
from .. import util
from pymdownx import betterem
import re
import time


class TestBetterNoSmart(util.MdCase):
    """Test escaping cases for BetterEm without smart enabled."""

    extension = [
        'pymdownx.betterem'
    ]
    extension_configs = {
        "pymdownx.betterem": {
            "smart_enable": "none"
        }
    }

    def test_complex_multple_emphasis_type(self):
        """Test complex case where `**text*text***` may be detected on accident."""

        self.check_markdown(
            'traced ***along*** bla **blocked** if other ***or***',
            '<p>traced <strong><em>along</em></strong> bla <strong>blocked</strong> if other <strong><em>or</em></strong></p>'  # noqa: E501
        )

    def test_complex_multple_emphasis_type_variant2(self):
        """Test another complex case where `**text*text***` may be detected on accident."""

        self.check_markdown(
            'on the **1-4 row** of the AP Combat Table ***and*** receive',
            '<p>on the <strong>1-4 row</strong> of the AP Combat Table <strong><em>and</em></strong> receive</p>'
        )

    def test_complex_multple_underscore_type(self):
        """Test complex case where `__text_text___` may be detected on accident."""

        self.check_markdown(
            'traced ___along___ bla __blocked__ if other ___or___',
            '<p>traced <strong><em>along</em></strong> bla <strong>blocked</strong> if other <strong><em>or</em></strong></p>'  # noqa: E501
        )

    def test_complex_multple_underscore_type_variant2(self):
        """Test another complex case where `__text_text___` may be detected on accident."""

        self.check_markdown(
            'on the __1-4 row__ of the AP Combat Table ___and___ receive',
            '<p>on the <strong>1-4 row</strong> of the AP Combat Table <strong><em>and</em></strong> receive</p>'
        )

    def test_complex_cases_star(self):
        """Test some complex cases for asterisks."""

        self.check_markdown(
            '''
            ***I'm italic and bold* I am just bold.**

            ***I'm bold and italic!** I am just italic.*

            *italic and **italic bold*** and *italic*

            **bold and *italic bold*** and *italic*

            ***I'm italic and bold* I am just bold.** *italic*

            ***I'm bold and italic!** I am just italic.* *italic*

            *italic and **italic bold*** and italic*

            **bold and *italic bold*** and bold*

            *italic and **italic bold***

            **bold and *italic bold***

            *italic **italic bold** italic*

            ***italic and bold* bold**: foo bar **italic**

            ***italic and bold** italic* foo bar **italic**

            *italic and **italic bold*** **italic**

            **bold and *italic bold*** **italic**
            ''',
            '''
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and <em>italic</em></p>
            <p><strong>bold and <em>italic bold</em></strong> and <em>italic</em></p>
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong> <em>italic</em></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em> <em>italic</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and italic*</p>
            <p><strong>bold and <em>italic bold</em></strong> and bold*</p>
            <p><em>italic and <strong>italic bold</strong></em></p>
            <p><strong>bold and <em>italic bold</em></strong></p>
            <p><em>italic <strong>italic bold</strong> italic</em></p>
            <p><strong><em>italic and bold</em> bold</strong>: foo bar <strong>italic</strong></p>
            <p><em><strong>italic and bold</strong> italic</em> foo bar <strong>italic</strong></p>
            <p><em>italic and <strong>italic bold</strong></em> <strong>italic</strong></p>
            <p><strong>bold and <em>italic bold</em></strong> <strong>italic</strong></p>
            ''',
            True
        )

    def test_complex_cases_underscore(self):
        """Test some complex cases for underscore."""

        self.check_markdown(
            '''
            ___I'm italic and bold_ I am just bold.__

            ___I'm bold and italic!__ I am just italic._

            _italic and __italic bold___ and _italic_

            __bold and _italic bold___ and _italic_

            ___I'm italic and bold_ I am just bold.__ _italic_

            ___I'm bold and italic!__ I am just italic._ _italic_

            _italic and __italic bold___ and italic_

            __bold and _italic bold___ and bold_

            _italic and __italic bold___

            __bold and _italic bold___

            _italic __italic bold__ italic_

            ___italic and bold_ bold__: foo bar __italic__

            ___italic and bold__ italic_ foo bar __italic__

            _italic and __italic bold___ __italic__

            __bold and _italic bold___ __italic__
            ''',
            '''
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and <em>italic</em></p>
            <p><strong>bold and <em>italic bold</em></strong> and <em>italic</em></p>
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong> <em>italic</em></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em> <em>italic</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and italic_</p>
            <p><strong>bold and <em>italic bold</em></strong> and bold_</p>
            <p><em>italic and <strong>italic bold</strong></em></p>
            <p><strong>bold and <em>italic bold</em></strong></p>
            <p><em>italic <strong>italic bold</strong> italic</em></p>
            <p><strong><em>italic and bold</em> bold</strong>: foo bar <strong>italic</strong></p>
            <p><em><strong>italic and bold</strong> italic</em> foo bar <strong>italic</strong></p>
            <p><em>italic and <strong>italic bold</strong></em> <strong>italic</strong></p>
            <p><strong>bold and <em>italic bold</em></strong> <strong>italic</strong></p>
            ''',
            True
        )


class TestBetterSmartAll(util.MdCase):
    """Test escaping cases for BetterEm with smart enabled everywhere."""

    extension = [
        'pymdownx.betterem'
    ]
    extension_configs = {
        "pymdownx.betterem": {
            "smart_enable": "all"
        }
    }

    def test_complex_cases_star(self):
        """Test some complex cases for asterisks."""

        self.check_markdown(
            '''
            ***I'm italic and bold* I am just bold.**

            ***I'm bold and italic!** I am just italic.*

            *italic and **italic bold*** and *italic*

            **bold and *italic bold*** and *italic*

            ***I'm italic and bold* I am just bold.** *italic*

            ***I'm bold and italic!** I am just italic.* *italic*

            *italic and **italic bold*** and not italic*

            **bold and *italic bold*** and not italic*

            *italic and **italic bold***

            **bold and *italic bold***

            *italic **italic bold** italic*

            ***italic and bold* bold**: foo bar **bold**

            ***italic and bold** italic* foo bar **bold**

            *italic and **italic bold*** **bold**

            **bold and *italic bold*** **bold**
            ''',
            '''
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and <em>italic</em></p>
            <p><strong>bold and <em>italic bold</em></strong> and <em>italic</em></p>
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong> <em>italic</em></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em> <em>italic</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and not italic*</p>
            <p><strong>bold and <em>italic bold</em></strong> and not italic*</p>
            <p><em>italic and <strong>italic bold</strong></em></p>
            <p><strong>bold and <em>italic bold</em></strong></p>
            <p><em>italic <strong>italic bold</strong> italic</em></p>
            <p><strong><em>italic and bold</em> bold</strong>: foo bar <strong>bold</strong></p>
            <p><em><strong>italic and bold</strong> italic</em> foo bar <strong>bold</strong></p>
            <p><em>italic and <strong>italic bold</strong></em> <strong>bold</strong></p>
            <p><strong>bold and <em>italic bold</em></strong> <strong>bold</strong></p>
            ''',
            True
        )

    def test_complex_cases_underscore(self):
        """Test some complex cases for underscore."""

        self.check_markdown(
            '''
            ___I'm italic and bold_ I am just bold.__

            ___I'm bold and italic!__ I am just italic._

            _italic and __italic bold___ and _italic_

            __bold and _italic bold___ and _italic_

            ___I'm italic and bold_ I am just bold.__ _italic_

            ___I'm bold and italic!__ I am just italic._ _italic_

            _italic and __italic bold___ and not italic_

            __bold and _italic bold___ and not italic_

            _italic and __italic bold___

            __bold and _italic bold___

            _italic __italic bold__ italic_

            ___italic and bold_ bold__: foo bar __bold__

            ___italic and bold__ italic_ foo bar __bold__

            _italic and __italic bold___ __bold__

            __bold and _italic bold___ __bold__
            ''',
            '''
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and <em>italic</em></p>
            <p><strong>bold and <em>italic bold</em></strong> and <em>italic</em></p>
            <p><strong><em>I'm italic and bold</em> I am just bold.</strong> <em>italic</em></p>
            <p><em><strong>I'm bold and italic!</strong> I am just italic.</em> <em>italic</em></p>
            <p><em>italic and <strong>italic bold</strong></em> and not italic_</p>
            <p><strong>bold and <em>italic bold</em></strong> and not italic_</p>
            <p><em>italic and <strong>italic bold</strong></em></p>
            <p><strong>bold and <em>italic bold</em></strong></p>
            <p><em>italic <strong>italic bold</strong> italic</em></p>
            <p><strong><em>italic and bold</em> bold</strong>: foo bar <strong>bold</strong></p>
            <p><em><strong>italic and bold</strong> italic</em> foo bar <strong>bold</strong></p>
            <p><em>italic and <strong>italic bold</strong></em> <strong>bold</strong></p>
            <p><strong>bold and <em>italic bold</em></strong> <strong>bold</strong></p>
            ''',
            True
        )


class TestBetterEmCatastrophicBacktracking(util.MdCase):
    """Test that unclosed delimiter runs are rejected without catastrophic backtracking."""

    extension = [
        'pymdownx.betterem'
    ]
    extension_configs = {}

    def assert_fast_no_match(self, pattern, text):
        """Assert that the pattern rejects the text well within a second."""

        start = time.perf_counter()
        self.assertIsNone(re.compile(pattern, re.DOTALL | re.UNICODE).match(text))
        self.assertLess(time.perf_counter() - start, 1.0)

    def test_star_em2(self):
        """Test that `*a` followed by a long run of asterisks is rejected quickly."""

        self.assert_fast_no_match(betterem.STAR_EM2, '*a' + '*' * 42 + 'b')

    def test_under_em2(self):
        """Test that `_a` followed by a long run of underscores is rejected quickly."""

        self.assert_fast_no_match(betterem.UNDER_EM2, '_a' + '_' * 42 + 'b')

    def test_smart_star_em2(self):
        """Test that `*a` followed by a long run of asterisks is rejected quickly in smart mode."""

        self.assert_fast_no_match(betterem.SMART_STAR_EM2, '*a' + '*' * 42 + 'b')

    def test_smart_under_em2(self):
        """Test that `_a` followed by a long run of underscores is rejected quickly in smart mode."""

        self.assert_fast_no_match(betterem.SMART_UNDER_EM2, '_a' + '_' * 42 + 'b')

    def test_unclosed_underscore_run(self):
        """Test that a long unclosed underscore run renders quickly with the default configuration."""

        text = '_a' + '_' * 42 + 'b'
        start = time.perf_counter()
        self.check_markdown(text, '<p>{}</p>'.format(text))
        self.assertLess(time.perf_counter() - start, 1.0)

    def test_unclosed_asterisk_runs(self):
        """Test that repeated unclosed asterisk runs render quickly with the default configuration."""

        start = time.perf_counter()
        html = self.md.convert('*a' + '*****b' * 16)
        self.assertLess(time.perf_counter() - start, 1.0)
        self.assertTrue(html.startswith('<p>') and html.endswith('</p>'))
