import pytest
from kelulusan import evaluasi_kelulusan

def test_lulus_standar():
    assert evaluasi_kelulusan(80, 70, "Lunas") == "LULUS"

def test_gagal_kehadiran():
    assert evaluasi_kelulusan(70, 90, "Lunas") == "TIDAK LULUS"

def test_gagal_nilai():
    assert evaluasi_kelulusan(90, 55, "Lunas") == "TIDAK LULUS"

def test_gagal_pembayaran():
    assert evaluasi_kelulusan(90, 90, "Belum Lunas") == "TIDAK LULUS"

def test_boundary_lulus():
    assert evaluasi_kelulusan(75, 60, "Lunas") == "LULUS"
