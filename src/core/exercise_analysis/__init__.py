"""
Exercise analysis package for form validation and movement analysis.
"""

from .squat_analyzer_base import (
    SquatAnalyzerBase,
    SquatPhase,
    SQUAT_VIEW_ANALYZER_REGISTRY,
    SideSquatAnalyzer,
    FrontSquatAnalyzer,
    SquatAnalyzer
)

__all__ = [
    'SquatAnalyzerBase',
    'SquatPhase',
    'SideSquatAnalyzer',
    'FrontSquatAnalyzer',
    'SQUAT_VIEW_ANALYZER_REGISTRY',
    'SquatAnalyzer'
]