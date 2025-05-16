from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = ".inventory_item"
        self.add_to_cart_buttons = ".btn_inventory"
        self.cart_icon = ".shopping_cart_link"

    def get_inventory_items_count(self) -> int:
        return len(self.page.query_selector_all(self.inventory_items))

    def add_item_to_cart(self, item_index: int):
        buttons = self.page.query_selector_all(self.add_to_cart_buttons)
        if 0 <= item_index < len(buttons):
            buttons[item_index].click()

    def go_to_cart(self):
        self.page.click(self.cart_icon)

    def sort_products(self,sort_option: str):
        self.page.select_option(".product_sort_container",sort_option)

    def get_product_names(self) -> list[str]:
        return self.page.eval_on_selector_all(".inventory_item_name", "elements => elements.map(e => e.innerText)")