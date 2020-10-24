public function generateSubOrders(){
    $order_items = this->items;
    foreach($item as $order_items){
        $product = DB::table('products')->where('id', $item->product_id)->get()[0]
        if($product->shop_id){
            $shop = Shop::find($product->shop_id);

            $suborder = $this->subOrders()->create([
                'order_id' => $this->id,
                'seller_id' => $shop->user_id,
                'grand_total' => $products->sum('pivot.price'),
                'item_count' => $products->count()
            ]);

            
            $suborder->items()->attach($product->id, ['price' => $product->pivot->price, 'quantity' => $product->pivot->quantity]);
        }
        if($product->wholesale_id){
            $shop = Shop::find($product->wholesale_id);

            $suborder = $this->subOrders()->create([
                'order_id' => $this->id,
                'seller_id' => $shop->user_id,
                'grand_total' => $products->sum('pivot.price'),
                'item_count' => $products->count(),
                'seller_type' => $product->wholesale_id
            ]);

            
            $suborder->items()->attach($product->id, ['price' => $product->pivot->price, 'quantity' => $product->pivot->quantity]);
        }   
    }
}