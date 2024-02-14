#!/usr/bin/env python

"""Tests for `Movie_recommendation_system` package."""


import unittest
from click.testing import CliRunner

from Movie_recommendation_system import Movie_recommendation_system
from Movie_recommendation_system import cli


class TestMovie_recommendation_system(unittest.TestCase):
    """Tests for `Movie_recommendation_system` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'Movie_recommendation_system.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
