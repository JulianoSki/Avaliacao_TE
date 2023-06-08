import unittest
from atividade_projeto import EquipmentManager


class EquipmentManagerTest(unittest.TestCase):

    def setUp(self):
        self.manager = EquipmentManager()

    def test_add_equipment(self):
        equipamento_id = self.manager.add_equipmento(
            'Equipmento 1', 'Descrição 1')
        self.assertIsNotNone(equipamento_id)

    def test_get_equipment(self):
        equipamento_id = self.manager.add_equipmento(
            'Equipmento 2', 'Descrição 2')
        equipmento = self.manager.get_equipmento(equipamento_id)
        self.assertEqual(equipmento['nome'], 'Equipmento 2')
        self.assertEqual(equipmento['descrição'], 'Descrição 2')

    def test_update_equipment(self):
        equipamento_id = self.manager.add_equipmento(
            'Equipmento 3', 'Descrição 3')
        self.manager.update_equipmento(equipamento_id, name='Novo equipamento')
        equipmento = self.manager.get_equipmento(equipamento_id)
        self.assertEqual(equipmento['nome'], 'Novo equipamento')

    def test_delete_equipment(self):
        equipamento_id = self.manager.add_equipmento(
            'Equipmento 4', 'Descrição 4')
        self.manager.delete_equipmento(equipamento_id)
        equipmento = self.manager.get_equipmento(equipamento_id)
        self.assertIsNone(equipmento)


if __name__ == '__main__':
    unittest.main()
