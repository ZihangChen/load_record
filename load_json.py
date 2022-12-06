from db import get_db
from filswan_statistic import FilswanStatistic
import json

def load_json():
    session = get_db()
    try:
        with open('result.json', 'r') as f:
            lines = f.readlines()
            for line in lines:
                stats = json.loads(line)
                data = stats['response']
                stats = FilswanStatistic(updated_at=stats['time'], sp_quantity=data['swan_provider'], active_sp_quantity=data['active_storage_providers'], \
                    total_cid=data['total_cids'], active_storage_deals=data['total_files_archived'], daily_upload=data['daily_deals_processed'], total_upload=data['total_deals_processed'], \
                    total_sealed_storage=data['storage_data_onboard'], miners_receiving_deals=data['storage_providers_receiving_deals'], data_transfered=data['data_transferred'])
                session.add(stats)
    finally:
        session.commit()
        session.close()

if __name__ == "__main__":
    load_json()