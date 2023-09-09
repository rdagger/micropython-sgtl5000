"""This library is for debugging."""
from collections import OrderedDict


class DUMP:
    """SGTL5000 register dump.
    
    Usage:
        from sgtl5000_dump import DUMP
        dump = DUMP(codec)
        dump.print_all()"""

    def __init__(self, codec):
        """Constructor for SGTL5000 register dump.

        Args:
            codec(class): SGTL5000 codec
        """
        self.codec = codec

    def get_chip_id(self):
        v = self.codec.regs[self.codec.CHIP_ID]
        return OrderedDict({
            "CHIP_ID": bin(v)[2:],
            "PARTID": (v >> 8) & 0xFF,
            "REVID": v & 0xFF
        })

    def get_chip_dig_power(self):
        v = self.codec.regs[self.codec.CHIP_DIG_POWER]
        return OrderedDict({
            "CHIP_DIG_POWER": bin(v)[2:],
            "ADC_POWERUP": (v >> 6) & 0x01,
            "DAC_POWERUP": (v >> 5) & 0x01,
            "DAP_POWERUP": (v >> 4) & 0x01,
            "I2S_OUT_POWERUP": (v >> 2) & 0x01,
            "I2S_IN_POWERUP": v & 0x01
        })

    def get_chip_clk_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_CLK_CTRL]
        return OrderedDict({
            "CHIP_CLK_CTRL": bin(v)[2:],
            "RATE_MODE": (v >> 4) & 0x03,
            "SYS_FS": (v >> 2) & 0x03,
            "MCLK_FREQ": v & 0x03
        })

    def get_chip_i2s_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_I2S_CTRL]
        return OrderedDict({
            "CHIP_I2S_CTRL": bin(v)[2:],
            "SCLKFREQ": (v >> 8) & 0x01,
            "MS": (v >> 7) & 0x01,
            "SCLK_INV": (v >> 6) & 0x01,
            "DLEN": (v >> 4) & 0x03,
            "I2S_MODE": (v >> 2) & 0x03,
            "LRALIGN": (v >> 1) & 0x01,
            "LRPOL": v & 0x01
        })

    def get_chip_sss_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_SSS_CTRL]
        return OrderedDict({
            "CHIP_SSS_CTRL": bin(v)[2:],
            "DAP_MIX_LRSWAP": (v >> 14) & 0x01,
            "DAP_LRSWAP": (v >> 13) & 0x01,
            "DAC_LRSWAP": (v >> 12) & 0x01,
            "I2S_LRSWAP": (v >> 10) & 0x01,
            "DAP_MIX_SELECT": (v >> 8) & 0x03,
            "DAP_SELECT": (v >> 6) & 0x03,
            "DAC_SELECT": (v >> 4) & 0x03,
            "I2S_SELECT": v & 0x03
        })

    def get_chip_adcdac_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_ADCDAC_CTRL]
        return OrderedDict({
            "CHIP_ADCDAC_CTRL": bin(v)[2:],
            "VOL_BUSY_DAC_RIGHT": (v >> 13) & 0x01,
            "VOL_BUSY_DAC_LEFT": (v >> 12) & 0x01,
            "VOL_RAMP_EN": (v >> 9) & 0x01,
            "VOL_EXPO_RAMP": (v >> 8) & 0x01,
            "DAC_MUTE_RIGHT": (v >> 3) & 0x01,
            "DAC_MUTE_LEFT": (v >> 2) & 0x01,
            "ADC_HPF_FREEZE": (v >> 1) & 0x01,
            "ADC_HPF_BYPASS": v & 0x01
        })

    def get_chip_dac_vol(self):
        v = self.codec.regs[self.codec.CHIP_DAC_VOL]
        return OrderedDict({
            "CHIP_DAC_VOL": bin(v)[2:],
            "DAC_VOL_RIGHT": (v >> 8) & 0xFF,
            "DAC_VOL_LEFT": v & 0xFF
        })

    def get_chip_pad_strength(self):
        v = self.codec.regs[self.codec.CHIP_PAD_STRENGTH]
        return OrderedDict({
            "CHIP_PAD_STRENGTH": bin(v)[2:],
            "I2S_LRCLK": (v >> 8) & 0x03,
            "I2S_SCLK": (v >> 6) & 0x03,
            "I2S_DOUT": (v >> 4) & 0x03,
            "CTRL_DATA": (v >> 2) & 0x03,
            "CTRL_CLK": v & 0x03
        })

    def get_chip_ana_adc_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_ANA_ADC_CTRL]
        return OrderedDict({
            "CHIP_ANA_ADC_CTRL": bin(v)[2:],
            "ADC_VOL_M6DB": (v >> 8) & 0x01,
            "ADC_VOL_RIGHT": (v >> 4) & 0x0F,
            "ADC_VOL_LEFT": v & 0x0F
        })

    def get_chip_ana_hp_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_ANA_HP_CTRL]
        return OrderedDict({
            "CHIP_ANA_HP_CTRL": bin(v)[2:],
            "HP_VOL_RIGHT": (v >> 8) & 0x7F,
            "HP_VOL_LEFT": v & 0x7F
        })

    def get_chip_ana_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_ANA_CTRL]
        return OrderedDict({
            "CHIP_ANA_CTRL": bin(v)[2:],
            "MUTE_LO": (v >> 8) & 0x01,
            "SELECT_HP": (v >> 6) & 0x01,
            "EN_ZCD_HP": (v >> 5) & 0x01,
            "MUTE_HP": (v >> 4) & 0x01,
            "SELECT_ADC": (v >> 2) & 0x01,
            "EN_ZCD_ADC": (v >> 1) & 0x01,
            "MUTE_ADC": v & 0x01
        })

    def get_chip_linreg_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_LINREG_CTRL]
        return OrderedDict({
            "CHIP_LINREG_CTRL": bin(v)[2:],
            "VDDC_MAN_ASSN": (v >> 6) & 0x01,
            "VDDC_ASSN_OVRD": (v >> 5) & 0x01,
            "D_PROGRAMMING": v & 0x0F
        })

    def get_chip_ref_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_REF_CTRL]
        return OrderedDict({
            "CHIP_REF_CTRL": bin(v)[2:],
            "VAG_VAL": (v >> 4) & 0x1F,
            "BIAS_CTRL": (v >> 1) & 0x07,
            "SMALL_POP": v & 0x01
        })

    def get_chip_mic_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_MIC_CTRL]
        return OrderedDict({
            "CHIP_MIC_CTRL": bin(v)[2:],
            "BIAS_RESISTOR": (v >> 8) & 0x03,
            "BIAS_VOLT": (v >> 4) & 0x07,
            "GAIN": v & 0x03
        })

    def get_chip_line_out_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_LINE_OUT_CTRL]
        return OrderedDict({
            "CHIP_LINE_OUT_CTRL": bin(v)[2:],
            "OUT_CURRENT": (v >> 8) & 0x0F,
            "LO_VAGCNTRL": v & 0x3F
        })

    def get_chip_line_out_vol(self):
        v = self.codec.regs[self.codec.CHIP_LINE_OUT_VOL]
        return OrderedDict({
            "CHIP_LINE_OUT_VOL": bin(v)[2:],
            "LO_VOL_RIGHT": (v >> 8) & 0x1F,
            "LO_VOL_LEFT": v & 0x1F
        })

    def get_chip_ana_power(self):
        v = self.codec.regs[self.codec.CHIP_ANA_POWER]
        return OrderedDict({
            "CHIP_ANA_POWER": bin(v)[2:],
            "DAC_MONO": (v >> 14) & 0x01,
            "LINREG_SIMPLE_POWERUP": (v >> 13) & 0x01,
            "STARTUP_POWERUP": (v >> 12) & 0x01,
            "VDDC_CHRGPMP_POWERUP": (v >> 11) & 0x01,
            "PLL_POWERUP": (v >> 10) & 0x01,
            "LINREG_D_POWERUP": (v >> 9) & 0x01,
            "VCOAMP_POWERUP": (v >> 8) & 0x01,
            "VAG_POWERUP": (v >> 7) & 0x01,
            "ADC_MONO": (v >> 6) & 0x01,
            "REFTOP_POWERUP": (v >> 5) & 0x01,
            "HEADPHONE_POWERUP": (v >> 4) & 0x01,
            "DAC_POWERUP": (v >> 3) & 0x01,
            "CAPLESS_HEADPHONE_POWERUP": (v >> 2) & 0x01,
            "ADC_POWERUP": (v >> 1) & 0x01,
            "LINEOUT_POWERUP": v & 0x01
        })

    def get_chip_pll_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_PLL_CTRL]
        return OrderedDict({
            "CHIP_PLL_CTRL": bin(v)[2:],
            "INT_DIVISOR": (v >> 11) & 0x1F,
            "FRAC_DIVISOR": v & 0x07FF
        })

    def get_chip_clk_top_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_CLK_TOP_CTRL]
        return OrderedDict({
            "CHIP_CLK_TOP_CTRL": bin(v)[2:],
            "ENABLE_INT_OSC": (v >> 11) & 0x01,
            "INPUT_FREQ_DIV2": (v >> 3) & 0x01
        })

    def get_chip_ana_status(self):
        v = self.codec.regs[self.codec.CHIP_ANA_STATUS]
        return OrderedDict({
            "CHIP_ANA_STATUS": bin(v)[2:],
            "LRSHORT_STS": (v >> 9) & 0x01,
            "CSHORT_STS": (v >> 8) & 0x01,
            "PLL_IS_LOCKED": (v >> 4) & 0x01
        })

    def get_chip_ana_test1(self):
        v = self.codec.regs[self.codec.CHIP_ANA_TEST1]
        return OrderedDict({
            "CHIP_ANA_TEST1": bin(v)[2:],
            "HP_IALL_ADJ": (v >> 14) & 0x03,
            "HP_I1_ADJ": (v >> 12) & 0x03,
            "HP_ANTIPOP": (v >> 9) & 0x03,
            "HP_CLASSAB": (v >> 8) & 0x01,
            "HP_HOLD_GND_CENTER": (v >> 7) & 0x01,
            "HP_HOLD_GND": (v >> 6) & 0x01,
            "VAG_DOUB_CURRENT": (v >> 5) & 0x01,
            "VAG_CLASSA": (v >> 4) & 0x01,
            "TM_ADCIN_TOHP": (v >> 3) & 0x01,
            "TM_HPCOMMON": (v >> 2) & 0x01,
            "TM_SELECT_MIC": (v >> 1) & 0x01,
            "TESTMODE": v & 0x01
        })

    def get_chip_ana_test2(self):
        v = self.codec.regs[self.codec.CHIP_ANA_TEST2]
        return OrderedDict({
            "CHIP_ANA_TEST2": bin(v)[2:],
            "LINEOUT_TO_VDDA": (v >> 14) & 0x01,
            "SPARE": (v >> 13) & 0x01,
            "MONOMODE_DAC": (v >> 12) & 0x01,
            "VCO_TUNE_AGAIN": (v >> 11) & 0x01,
            "LO_PASS_MASTERVAG": (v >> 10) & 0x01,
            "INVERT_DAC_SAMPLE_CLOCK": (v >> 9) & 0x01,
            "INVERT_DAC_DATA_TIMING": (v >> 8) & 0x01,
            "DAC_EXTEND_RTZ": (v >> 7) & 0x01,
            "DAC_DOUBLE_I": (v >> 6) & 0x01,
            "DAC_DIS_RTZ": (v >> 5) & 0x01,
            "DAC_CLASSA": (v >> 4) & 0x01,
            "INVERT_ADC_SAMPLE_CLOCK": (v >> 3) & 0x01,
            "INVERT_ADC_DATA_TIMING": (v >> 2) & 0x01,
            "ADC_LESSI": (v >> 1) & 0x01,
            "ADC_DITHEROFF": v & 0x01
        })

    def get_chip_short_ctrl(self):
        v = self.codec.regs[self.codec.CHIP_SHORT_CTRL]
        return OrderedDict({
            "CHIP_SHORT_CTRL": bin(v)[2:],
            "LVLADJR": (v >> 12) & 0x07,
            "LVLADJL": (v >> 8) & 0x07,
            "LVLADJC": (v >> 4) & 0x07,
            "MODE_LR": (v >> 3) & 0x03,
            "MODE_CM": v & 0x03
        })

    def get_dap_control(self):
        v = self.codec.regs[self.codec.DAP_CONTROL]
        return OrderedDict({
            "DAP_CONTROL": bin(v)[2:],
            "MIX_EN": (v >> 4) & 0x01,
            "DAP_EN": v & 0x01
        })

    def get_dap_peq(self):
        v = self.codec.regs[self.codec.DAP_PEQ]
        return OrderedDict({
            "DAP_PEQ": bin(v)[2:],
            "EN": v & 0x07
        })

    def get_dap_bass_enhance(self):
        v = self.codec.regs[self.codec.DAP_BASS_ENHANCE]
        return OrderedDict({
            "DAP_BASS_ENHANCE": bin(v)[2:],
            "BYPASS_HPF": (v >> 8) & 0x01,
            "CUTOFF": (v >> 4) & 0x07,
            "EN": v & 0x01
        })

    def get_dap_bass_enhance_ctrl(self):
        v = self.codec.regs[self.codec.DAP_BASS_ENHANCE_CTRL]
        return OrderedDict({
            "DAP_BASS_ENHANCE_CTRL": bin(v)[2:],
            "LR_LEVEL": (v >> 8) & 0x3F,
            "BASS_LEVEL": v & 0x7F
        })

    def get_dap_audio_eq(self):
        v = self.codec.regs[self.codec.DAP_AUDIO_EQ]
        return OrderedDict({
            "DAP_AUDIO_EQ": bin(v)[2:],
            "EN": v & 0x03
        })

    def get_dap_sgtl_surround(self):
        v = self.codec.regs[self.codec.DAP_SGTL_SURROUND]
        return OrderedDict({
            "DAP_SGTL_SURROUND": bin(v)[2:],
            "WIDTH_CONTROL": (v >> 4) & 0x07,
            "SELECT": v & 0x03
        })

    def get_dap_filter_coef_access(self):
        v = self.codec.regs[self.codec.DAP_FILTER_COEF_ACCESS]
        return OrderedDict({
            "DAP_FILTER_COEF_ACCESS": bin(v)[2:],
            "WR": (v >> 8) & 0x01,
            "INDEX": v & 0xFF
        })

    def get_dap_coef_wr_b0_msb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_B0_MSB]
        return OrderedDict({
            "DAP_COEF_WR_B0_MSB": bin(v)[2:]
        })

    def get_dap_coef_wr_b0_lsb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_B0_LSB]
        return OrderedDict({
            "DAP_COEF_WR_B0_LSB": bin(v)[2:],
            "LSB4": v & 0x0F
        })

    def get_dap_audio_eq_bass_band0(self):
        v = self.codec.regs[self.codec.DAP_AUDIO_EQ_BASS_BAND0]
        return OrderedDict({
            "DAP_AUDIO_EQ_BASS_BAND0": bin(v)[2:],
            "VOLUME": v & 0x7F
        })

    def get_dap_audio_eq_band1(self):
        v = self.codec.regs[self.codec.DAP_AUDIO_EQ_BAND1]
        return OrderedDict({
            "DAP_AUDIO_EQ_BAND1": bin(v)[2:],
            "VOLUME": v & 0x7F
        })

    def get_dap_audio_eq_band2(self):
        v = self.codec.regs[self.codec.DAP_AUDIO_EQ_BAND2]
        return OrderedDict({
            "DAP_AUDIO_EQ_BAND2": bin(v)[2:],
            "VOLUME": v & 0x7F
        })

    def get_dap_audio_eq_band3(self):
        v = self.codec.regs[self.codec.DAP_AUDIO_EQ_BAND3]
        return OrderedDict({
            "DAP_AUDIO_EQ_BAND3": bin(v)[2:],
            "VOLUME": v & 0x7F
        })

    def get_dap_audio_eq_treble_band4(self):
        v = self.codec.regs[self.codec.DAP_AUDIO_EQ_TREBLE_BAND4]
        return OrderedDict({
            "DAP_AUDIO_EQ_TREBLE_BAND4": bin(v)[2:],
            "VOLUME": v & 0x7F
        })

    def get_dap_main_chan(self):
        v = self.codec.regs[self.codec.DAP_MAIN_CHAN]
        return OrderedDict({
            "DAP_MAIN_CHAN": bin(v)[2:],
            "VOL": v & 0xFFFF
        })

    def get_dap_mix_chan(self):
        v = self.codec.regs[self.codec.DAP_MIX_CHAN]
        return OrderedDict({
            "DAP_MIX_CHAN": bin(v)[2:],
            "VOL": v & 0xFFFF
        })

    def get_dap_avc_ctrl(self):
        v = self.codec.regs[self.codec.DAP_AVC_CTRL]
        return OrderedDict({
            "DAP_AVC_CTRL": bin(v)[2:],
            "MAX_GAIN": (v >> 12) & 0x07,
            "LBI_RESPONSE": (v >> 8) & 0x03,
            "HARD_LIMIT_EN": (v >> 5) & 0x01,
            "EN": v & 0x01
        })

    def get_dap_avc_threshold(self):
        v = self.codec.regs[self.codec.DAP_AVC_THRESHOLD]
        return OrderedDict({
            "DAP_AVC_THRESHOLD": bin(v)[2:]
        })

    def get_dap_avc_attack(self):
        v = self.codec.regs[self.codec.DAP_AVC_ATTACK]
        return OrderedDict({
            "DAP_AVC_ATTACK": bin(v)[2:],
            "RATE": v & 0x0FFF
        })

    def get_dap_avc_decay(self):
        v = self.codec.regs[self.codec.DAP_AVC_DECAY]
        return OrderedDict({
            "DAP_AVC_DECAY": bin(v)[2:],
            "RATE": v & 0x0FFF
        })

    def get_dap_coef_wr_b1_msb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_B1_MSB]
        return OrderedDict({
            "DAP_COEF_WR_B1_MSB": bin(v)[2:]
        })

    def get_dap_coef_wr_b1_lsb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_B1_LSB]
        return OrderedDict({
            "DAP_COEF_WR_B1_LSB": bin(v)[2:],
            "LSB4": v & 0x0FFF
        })

    def get_dap_coef_wr_b2_msb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_B2_MSB]
        return OrderedDict({
            "DAP_COEF_WR_B2_MSB": bin(v)[2:]
        })

    def get_dap_coef_wr_b2_lsb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_B2_LSB]
        return OrderedDict({
            "DAP_COEF_WR_B2_LSB": bin(v)[2:],
            "LSB4": v & 0x0FFF
        })

    def get_dap_coef_wr_a1_msb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_A1_MSB]
        return OrderedDict({
            "DAP_COEF_WR_A1_MSB": bin(v)[2:]
        })

    def get_dap_coef_wr_a1_lsb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_A1_LSB]
        return OrderedDict({
            "DAP_COEF_WR_A1_LSB": bin(v)[2:],
            "LSB4": v & 0x0FFF
        })

    def get_dap_coef_wr_a2_msb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_A2_MSB]
        return OrderedDict({
            "DAP_COEF_WR_A2_MSB": bin(v)[2:]
        })

    def get_dap_coef_wr_a2_lsb(self):
        v = self.codec.regs[self.codec.DAP_COEF_WR_A2_LSB]
        return OrderedDict({
            "DAP_COEF_WR_A2_LSB": bin(v)[2:],
            "LSB4": v & 0x0FFF
        })

    def print_all(self):
        """Prints all SGTL5000 registers."""
        method_list = [func for func in dir(DUMP) if callable(getattr(DUMP, func)) and func.startswith("get_")]
        for method in method_list:
            results = getattr(self, method)()
            for i, (k, v) in enumerate(results.items()):
                if i != 0:
                    print("\t", end=" ")
                print(f"{k}: {v}")
