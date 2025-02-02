from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.ledger import \
    GenesisResponse


def test_genesis(requests_mock):
    api = BlockFrostApi()
    mock_data = {
        "active_slots_coefficient": 0.05,
        "update_quorum": 5,
        "max_lovelace_supply": "45000000000000000",
        "network_magic": 764824073,
        "epoch_length": 432000,
        "system_start": 1506203091,
        "slots_per_kes_period": 129600,
        "slot_length": 1,
        "max_kes_evolutions": 62,
        "security_param": 2160
    }
    requests_mock.get(f"{api.url}/genesis", json=mock_data)
    mock_object = GenesisResponse(**mock_data)
    assert api.genesis() == mock_object
