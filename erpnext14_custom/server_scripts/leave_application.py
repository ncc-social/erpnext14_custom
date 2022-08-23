from typing import Dict, Optional, Tuple

import frappe
from frappe import _
from frappe.query_builder.functions import Max, Min, Sum
from frappe.utils import (
	add_days,
	cint,
	cstr,
	date_diff,
	flt,
	formatdate,
	get_fullname,
	get_link_to_form,
	getdate,
	nowdate,
)

from erpnext.buying.doctype.supplier_scorecard.supplier_scorecard import daterange
from erpnext.setup.doctype.employee.employee import get_holiday_list_for_employee
from hrms.hr.doctype.leave_block_list.leave_block_list import get_applicable_block_dates
from hrms.hr.doctype.leave_ledger_entry.leave_ledger_entry import create_leave_ledger_entry
from hrms.hr.utils import (
	get_holiday_dates_for_employee,
	get_leave_period,
	set_employee_name,
	share_doc_with_approver,
	validate_active_employee,
)

def after_approval(self):
	if self.status == "Open":
		frappe.throw(_("Only Leave Applications with status 'Approved' and 'Rejected' can be submitted"))
	self.validate_back_dated_application()

# notify leave applier about approval
	if frappe.db.get_single_value("HR Settings", "send_leave_notification"):
		self.notify_employee()

	self.create_leave_ledger_entry()
	self.reload()

def validate_back_dated_application(self):
    future_allocation = frappe.db.sql("""select name, from_date from `tabLeave Allocation`
			where employee=%s and leave_type=%s and docstatus=1 and from_date > %s
			and carry_forward=1""", (self.employee, self.leave_type, self.to_date), as_dict=1)

    if future_allocation:
        frappe.throw(_("Leave cannot be applied/cancelled before {0}, as leave balance has already been carry-forwarded in the future leave allocation record {1}")
            .format(formatdate(future_allocation[0].from_date), future_allocation[0].name))
