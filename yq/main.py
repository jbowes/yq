# vi:si:et:sw=4:sts=4:ts=4

import sys

from yq.util import command
from yq.util import config

from yq.command import init
from yq.command import new
from yq.command import refresh
from yq.command import pop
from yq.command import push
from yq.command import top
from yq.command import helpcmd
from yq.command import series
from yq.command import applied
from yq.command import show
from yq.command import next
from yq.command import prev
from yq.command import pending


class Yq(command.Command):
    usage = "%prog %command"
    description = """yq is quilt for packages."""

    subCommandClasses = [init.Init, new.New, refresh.Refresh, pop.Pop,
            push.Push, top.Top, helpcmd.Help, series.Series, applied.Applied,
            show.Show, next.Next, prev.Prev, pending.Pending]

    def addOptions(self):
        self.parser.add_option('', '--version', action="store_true",
                help="show version information")

    def handleOptions(self, options):
        if options.version:
            print >> self.stdout, config.VERSION
            sys.exit(0)


def main(argv):
    c = Yq()
    try:
        ret = c.parse(argv)
    except SystemError, e:
        sys.stderr.write('yq: error: %s\n' % e.args)
        return 255

    if ret is None:
        return 0
    return ret
