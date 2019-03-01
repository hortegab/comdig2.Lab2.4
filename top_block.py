#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Description: NOTAS: Spp es samples per period; p_correccionla correcion de fase no esta en grados sino en muestras;
# Generated: Fri Mar  1 06:23:42 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.fmensaje = fmensaje = 30
        self.fc = fc = 1000
        self.BW_mensaje = BW_mensaje = fmensaje*16
        self.samp_rate = samp_rate = math.ceil((fc+BW_mensaje)*8.)
        self.p_correccion = p_correccion = 0
        self.f_dev_in = f_dev_in = 0
        self.f_correccion = f_correccion = 0
        self.Spp = Spp = int(math.ceil(samp_rate/fc))
        self.Ac_in = Ac_in = 1

        ##################################################
        # Blocks
        ##################################################
        self._p_correccion_range = Range(0, Spp, 1, 0, 200)
        self._p_correccion_win = RangeWidget(self._p_correccion_range, self.set_p_correccion, "p_correccion", "counter_slider", int)
        self.top_grid_layout.addWidget(self._p_correccion_win)
        self._f_dev_in_range = Range(-BW_mensaje/2., BW_mensaje/2., BW_mensaje/200., 0, 200)
        self._f_dev_in_win = RangeWidget(self._f_dev_in_range, self.set_f_dev_in, "f_dev_in", "counter_slider", float)
        self.top_grid_layout.addWidget(self._f_dev_in_win)
        self._f_correccion_range = Range(-BW_mensaje/2., BW_mensaje/2., BW_mensaje/200., 0, 200)
        self._f_correccion_win = RangeWidget(self._f_correccion_range, self.set_f_correccion, "f_correccion", "counter_slider", float)
        self.top_grid_layout.addWidget(self._f_correccion_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Error de sincronismo", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-0.04, 0.04)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['I', 'Q', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.low_pass_filter_0_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, BW_mensaje, BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, BW_mensaje, BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, BW_mensaje, BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.desfase_0 = blocks.delay(gr.sizeof_float*1, p_correccion)
        self.desfase = blocks.delay(gr.sizeof_float*1, p_correccion)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fmensaje, 0.3, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fc+f_correccion, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fc+f_correccion, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fc+f_dev_in, Ac_in, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.desfase_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.desfase, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.desfase, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.desfase_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_2, 1))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_multiply_xx_0_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_fmensaje(self):
        return self.fmensaje

    def set_fmensaje(self, fmensaje):
        self.fmensaje = fmensaje
        self.set_BW_mensaje(self.fmensaje*16)
        self.analog_sig_source_x_1.set_frequency(self.fmensaje)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.set_Spp(int(math.ceil(self.samp_rate/self.fc)))
        self.set_samp_rate(math.ceil((self.fc+self.BW_mensaje)*8.))
        self.analog_sig_source_x_0_0_0.set_frequency(self.fc+self.f_correccion)
        self.analog_sig_source_x_0_0.set_frequency(self.fc+self.f_correccion)
        self.analog_sig_source_x_0.set_frequency(self.fc+self.f_dev_in)

    def get_BW_mensaje(self):
        return self.BW_mensaje

    def set_BW_mensaje(self, BW_mensaje):
        self.BW_mensaje = BW_mensaje
        self.set_samp_rate(math.ceil((self.fc+self.BW_mensaje)*8.))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, self.BW_mensaje, self.BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW_mensaje, self.BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW_mensaje, self.BW_mensaje/8., firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Spp(int(math.ceil(self.samp_rate/self.fc)))
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, self.BW_mensaje, self.BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW_mensaje, self.BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW_mensaje, self.BW_mensaje/8., firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_p_correccion(self):
        return self.p_correccion

    def set_p_correccion(self, p_correccion):
        self.p_correccion = p_correccion
        self.desfase_0.set_dly(self.p_correccion)
        self.desfase.set_dly(self.p_correccion)

    def get_f_dev_in(self):
        return self.f_dev_in

    def set_f_dev_in(self, f_dev_in):
        self.f_dev_in = f_dev_in
        self.analog_sig_source_x_0.set_frequency(self.fc+self.f_dev_in)

    def get_f_correccion(self):
        return self.f_correccion

    def set_f_correccion(self, f_correccion):
        self.f_correccion = f_correccion
        self.analog_sig_source_x_0_0_0.set_frequency(self.fc+self.f_correccion)
        self.analog_sig_source_x_0_0.set_frequency(self.fc+self.f_correccion)

    def get_Spp(self):
        return self.Spp

    def set_Spp(self, Spp):
        self.Spp = Spp

    def get_Ac_in(self):
        return self.Ac_in

    def set_Ac_in(self, Ac_in):
        self.Ac_in = Ac_in
        self.analog_sig_source_x_0.set_amplitude(self.Ac_in)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
