from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from legendary.core import LegendaryCore

from Rare.Components.Tabs.Games.GameWidgetInstalled import GameWidgetInstalled
from Rare.Components.Tabs.Games.GameWidgetUninstalled import GameWidgetUninstalled
from Rare.utils.QtExtensions import FlowLayout


class GameList(QScrollArea):
    def __init__(self, core: LegendaryCore):
        super(GameList, self).__init__()
        self.core = core
        self.widget = QWidget()
        self .setObjectName("list_widget")
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.layout = FlowLayout()

        for i in self.core.get_installed_list():
            # continue
            self.layout.addWidget(GameWidgetInstalled(core, i))

        uninstalled_games = []
        installed = [i.app_name for i in core.get_installed_list()]
        for game in sorted(core.get_game_list(), key=lambda x: x.app_title):
            if not game.app_name in installed:
                uninstalled_games.append(game)
        self.widgets = []

        for i in uninstalled_games:
            widget = GameWidgetUninstalled(core, i)
            self.layout.addWidget(widget)
            self.widgets.append(widget)

        self.widget.setLayout(self.layout)
        self.setWidget(self.widget)

    def filter(self, text: str):
        for w in self.widgets:
            if text.lower() in w.game.app_title.lower() + w.game.app_name.lower():
                w.setVisible(True)
            else:
                w.setVisible(False)

    def installed_only(self, i_o: bool):
        # TODO save state
        for w in self.widgets:
            w.setVisible(not i_o)