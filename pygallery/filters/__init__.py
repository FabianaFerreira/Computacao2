from filters.bw_filter import BWFilter
from filters.gotham_filter import GothamFilter
from filters.vienna_filter import ViennaFilter
from filters.brno_filter import BrnoFilter

filters_dict = {
    'bw': BWFilter(),
    'gotham': GothamFilter(),
    'vienna': ViennaFilter(),
    'brno': BrnoFilter()
}
