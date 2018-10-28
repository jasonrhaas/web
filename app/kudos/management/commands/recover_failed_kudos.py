"""Define the mint all kudos management command.

Copyright (C) 2018 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
import logging
import time
import urllib
import time
import warnings

from django.conf import settings
from django.core.management.base import BaseCommand

import redis
import oyaml as yaml
from kudos.utils import KudosContract, get_rarity_score, humanize_name

warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("web3").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
formatter = '%(levelname)s:%(name)s.%(funcName)s:%(message)s'


class Command(BaseCommand):

    help = 'mints the initial kudos gen0 set'

    def add_arguments(self, parser):
        # parser.add_argument('network', default='localhost', type=str)
        parser.add_argument('redis_run_id', type=str)

    def handle(self, *args, **options):
        # network = options['network']
        redis_run_id = options['redis_run_id']
        redis_conn = redis.StrictRedis(host='redis', port=6379, db=9, decode_responses=True)
        path = 'kudos'
        yaml_file = f'{path}/kudos.yaml'
        with open(yaml_file) as f:
            all_kudos = yaml.load(f)

        failed_kudos_names = redis_conn.lrange(redis_run_id, 0, -1)

        if not failed_kudos_names:
            print(f'No failed kudos were found for {redis_run_id}')
            return False

        failed_kudos = []
        for idx, kudos in enumerate(all_kudos):
            if kudos['name'] in failed_kudos_names:
                failed_kudos.append(kudos)

        outfile = f'{path}/failed_kudos_{redis_run_id}.yaml'
        with open(outfile, 'w') as f:
            f.write(yaml.dump(failed_kudos, default_flow_style=False))

        print(f'Recovery file written to {outfile}')
        redis_conn.delete(redis_run_id)
