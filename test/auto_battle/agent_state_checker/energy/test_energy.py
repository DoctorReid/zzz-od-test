import test
from zzz_od.auto_battle.agent_state import agent_state_checker
from zzz_od.game_data.agent import CommonAgentStateEnum, AgentStateDef


class TestEnergy(test.ZzzTestBase):

    def __init__(self, *args, **kwargs):
        test.ZzzTestBase.__init__(self, *args, **kwargs)

    def test_energy(self):
        for total in [2, 3]:
            for pos in [1, 2, 3]:
                for cnt in [0, 60, 120]:
                    screen = self.get_test_image(f'{total}_{pos}_{cnt}')
                    if screen is None:
                        continue
                    state = self._get_state(total, pos)
                    ans = agent_state_checker.check_length_by_foreground_gray(self.ctx, screen, state)

                    print(total, pos, cnt, ans)
                    if cnt > 0:
                        self.assertTrue(ans >= cnt)
                    else:
                        self.assertEqual(cnt, ans)

    def _get_state(self, total: int, pos: int) -> AgentStateDef:
        if total == 3:
            if pos == 1:
                return CommonAgentStateEnum.ENERGY_31.value
            elif pos == 2:
                return CommonAgentStateEnum.ENERGY_32.value
            elif pos == 3:
                return CommonAgentStateEnum.ENERGY_33.value
        elif total == 2:
            if pos == 1:
                return CommonAgentStateEnum.ENERGY_21.value
            elif pos == 2:
                return CommonAgentStateEnum.ENERGY_22.value