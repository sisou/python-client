from .staker import Staker

__all__ = ["ParkedValidators", "Validator"]


class Validator:
    """
    Validator returned by the server

    :param address: Address of the validator.
    :type address: str
    :param warmAddress: Warm address of the validator.
    :type warmAddress: str
    :param signingKey: Signing key of the validator.
    :type signingKey: str
    :param votingKey: Voting key of the validator.
    :type votingKey: str
    :param rewardAddress: Reward address of the validator.
    :type rewardAddress: str
    :param balance: Balance of the validator.
    :type balance: int
    :param numStakers: Number of stakers for this validator.
    :type numStakers: int
    :param stakers: List of stakers represented by a Staker object.
    :type stakers: list of(Staker)
    """

    def __init__(self, address, signingKey, votingKey, rewardAddress, balance,
                 numStakers, inactivityFlag=None, signalData=None, stakers={}):
        self.address = address
        self.signingKey = signingKey
        self.votingKey = votingKey
        self.rewardAddress = rewardAddress
        self.balance = balance
        self.numStakers = numStakers
        self.inactivityFlag = inactivityFlag
        self.signalData = signalData
        staker_objs = []
        if type(stakers) is dict:
            for address, balance in stakers.items():
                staker_objs.append(Staker(address, balance))
        else:
            from ..nimiq_client import InternalErrorException
            raise InternalErrorException(
                "Couldn't parse Stakers {0}".format(stakers)
            )
        self.stakers = staker_objs


class ParkedValidators:
    """
    Parked validators returned by the server

    :param blockNumber: Block number in which the validators were parked.
    :type blockNumber: int
    :param validators: List of parked validators
    :type validators: List of (Validator)
    """

    def __init__(self, blockNumber, validators):
        self.blockNumber = blockNumber
        self.validators = [Validator(**validator) for validator in validators]
