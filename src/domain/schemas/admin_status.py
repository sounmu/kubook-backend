from collections import namedtuple
from enum import Enum

AdminStatusData = namedtuple('AdminStatusData', ['admin_status', 'description'])


class AdminStatus(str, Enum):
    ACTIVE = AdminStatusData("ACTIVE", "현재 활성화된 관리자입니다.")
    INACTIVE = AdminStatusData("INACTIVE", "현재 비활성화된 관리자입니다.")
    SUSPENDED = AdminStatusData("SUSPENDED", "현재 정지된 관리자입니다.")

    @property
    def admin_status(self):
        return self.value.admin_status

    @property
    def description(self):
        return self.value.description

# 사용 예시
# print(AdminStatus.ACTIVE.admin_status) # ACTIVE
# print(AdminStatus.ACTIVE.description) # 현재 활성화된 관리자입니다.
