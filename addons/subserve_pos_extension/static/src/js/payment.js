import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";

patch(PaymentScreen.prototype, {
  async validateOrder(isForceValidate) {
    const res = await super.validateOrder(isForceValidate);

    if (this.currentOrder.is_paid() &&
        this.currentOrder.get_paymentlines().some(p => p.payment_method.is_cash)) {
      this.env.services.hardware.openCashbox();
    }

    return res;
  }
});
