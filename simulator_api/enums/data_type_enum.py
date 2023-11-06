from aenum import MultiValueEnum


class DataTypeEnum(MultiValueEnum):
    _init_ = 'value builder_class'
    MULTIPLICATIVE = "multiplicative", "MultiplicativeBuilder"
    ADDITIVE = "additive", "AdditiveBuilder"
