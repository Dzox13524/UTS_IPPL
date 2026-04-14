import pytest
from hitungakademik import hitung_akademik

def test_valid_multi_parameter():
    case_1 = hitung_akademik(0, 0, 0)
    assert case_1['score'] == 0.0
    assert case_1['grade'] == 'E'

    case_2 = hitung_akademik(100, 100, 100)
    assert case_2['score'] == 100.0
    assert case_2['grade'] == 'A'

    case_3 = hitung_akademik(0, 100, 100)
    assert case_3['score'] == 70.0
    assert case_3['grade'] == 'C'

def test_boundary_values():
    hasil_min_plus = hitung_akademik(1, 1, 1)
    assert hasil_min_plus['score'] == 1.0
    
    hasil_max_minus = hitung_akademik(99, 99, 99)
    assert hasil_max_minus['score'] == 99.0
    assert hasil_max_minus['grade'] == 'A'

def test_out_of_bound():
    msg_error = "Error: Input harus berada dalam rentang 0-100"
    
    assert hitung_akademik(101, 70, 70) == msg_error
    assert hitung_akademik(70, -1, 70) == msg_error
    assert hitung_akademik(999999, 80, 80) == msg_error

def test_invalid_data_types():
    msg_error = "Error: Input harus bertipe numerik"
    
    assert hitung_akademik("A+", 80, 90) == msg_error
    assert hitung_akademik(True, 80, 80) == msg_error
    assert hitung_akademik(80, "#", 90) == msg_error

def test_null_input():
    msg_error = "Error: Input tidak boleh kosong"
    
    assert hitung_akademik(None, 70, 80) == msg_error
    assert hitung_akademik(None, None, None) == msg_error

def test_extreme_decimal():
    hasil = hitung_akademik(85.123456789, 80, 80)
    assert hasil['score'] == 81.54
