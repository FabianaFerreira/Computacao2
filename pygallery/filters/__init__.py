from filters.bw_filter import BWFilter
from filters.gotham_filter import GothamFilter
from filters.vienna_filter import ViennaFilter
from filters.brno_filter import BrnoFilter
from filters.pyeongchang_filter import PyeongChangFilter
from filters.sepia_filter import SepiaFilter
from filters.jacarta_filter import JacartaFilter
from filters.oslo_filter import OsloFilter

filter_list = [
    BWFilter(),
    GothamFilter(),
    ViennaFilter(),
    BrnoFilter(),
    PyeongChangFilter(),
    SepiaFilter(),
    JacartaFilter(),
    OsloFilter()
]
