from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mantra24_ultimate_key'

# Comprehensive Data with Subcategory Images
CATEGORIES_DATA = {
    'home': {
        'name': 'Home & Living', 
        'img': 'https://images.unsplash.com/photo-1484101403633-562f891dc89a?w=400',
        'sub_items': [
            {'name': 'Furniture', 'img': 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=400'},
            {'name': 'Home Décor', 'img': 'https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=400'},
            {'name': 'Kitchen & Dining', 'img': 'https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=400'},
            {'name': 'Bedding & Bath', 'img': 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400'},
            {'name': 'Storage', 'img': 'https://images.unsplash.com/photo-1594409445022-5a4096053961?w=400'}
        ]
    },
    'fashion': {
        'name': 'Fashion', 
        'img': 'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400',
        'sub_items': [
            {'name': "Men's Clothing", 'img': 'https://images.unsplash.com/photo-1490578474895-699cd4e2cf59?w=400'},
            {'name': "Women's Clothing", 'img': 'https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=400'},
            {'name': 'Shoes & Footwear', 'img': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400'},
            {'name': 'Accessories', 'img': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400'},
            {'name': 'Ethnic Wear', 'img': 'https://images.unsplash.com/photo-1583391733956-6c78276477e2?w=400'}
        ]
    },
    'electronics': {
        'name': 'Electronics', 
        'img': 'https://images.unsplash.com/photo-1498049794561-7780e7231661?w=400',
        'sub_items': [
            {'name': 'Mobile Phones', 'img': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400'},
            {'name': 'Laptops & Computers', 'img': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=400'},
            {'name': 'Audio Devices', 'img': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400'},
            {'name': 'Smart Wearables', 'img': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400'},
            {'name': 'Home Electronics', 'img': 'https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=400'}
        ]
    },
    'beauty': {
        'name': 'Beauty & Personal Care', 
        'img': 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400',
        'sub_items': [
            {'name': 'Skincare', 'img': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400'},
            {'name': 'Makeup', 'img': 'https://images.unsplash.com/photo-1522338253792-192feee2c786?w=400'},
            {'name': 'Hair Care', 'img': 'https://images.unsplash.com/photo-1527799822367-3188572f483f?w=400'},
            {'name': 'Fragrances', 'img': 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=400'},
            {'name': 'Personal Hygiene', 'img': 'https://images.unsplash.com/photo-1584622781564-1d9876a13d00?w=400'}
        ]
    },
    'health': {
        'name': 'Health & Wellness', 
        'img': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400',
        'sub_items': [
            {'name': 'Vitamins', 'img': 'https://images.unsplash.com/photo-1584017911766-d451b3d0e843?w=400'},
            {'name': 'Fitness Equipment', 'img': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400'},
            {'name': 'Health Monitors', 'img': 'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400'},
            {'name': 'Ayurvedic', 'img': 'https://images.unsplash.com/photo-1512103602290-d7d655a6082d?w=400'},
            {'name': 'Mental Wellness', 'img': 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400'}
        ]
    },
    'sports': {
        'name': 'Sports & Outdoors', 
        'img': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400',
        'sub_items': [
            {'name': 'Sportswear', 'img': 'https://images.unsplash.com/photo-1518310383802-640c2de311b2?w=400'},
            {'name': 'Camping & Hiking', 'img': 'https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?w=400'},
            {'name': 'Cycling', 'img': 'https://images.unsplash.com/photo-1485965120184-e220f721d03e?w=400'},
            {'name': 'Fitness Accessories', 'img': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=400'},
            {'name': 'Outdoor Games', 'img': 'https://images.unsplash.com/photo-1531415074968-036ba1b575da?w=400'}
        ]
    },
    'kids': {
        'name': 'Baby, Kids & Toys', 
        'img': 'https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?w=400',
        'sub_items': [
            {'name': 'Toys & Games', 'img': 'https://images.unsplash.com/photo-1536640712-4d4c36ff0e4e?w=400'},
            {'name': 'Baby Care', 'img': 'https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?w=400'},
            {'name': 'School Supplies', 'img': 'https://images.unsplash.com/photo-1503676260728-1c00da07bb5e?w=400'},
            {'name': 'Kids Clothing', 'img': 'https://images.unsplash.com/photo-1514090458221-65bb69cf63e6?w=400'},
            {'name': 'Learning', 'img': 'https://images.unsplash.com/photo-1503676260728-1c00da07bb5e?w=400'}
        ]
    },
    'grocery': {
        'name': 'Grocery & Essentials', 
        'img': 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=400',
        'sub_items': [
            {'name': 'Snacks', 'img': 'https://images.unsplash.com/photo-1599490659213-e2b9527bb087?w=400'},
            {'name': 'Beverages', 'img': 'https://images.unsplash.com/photo-1544145945-f904253db0ad?w=400'},
            {'name': 'Cleaning Supplies', 'img': 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400'},
            {'name': 'Daily Essentials', 'img': 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=400'},
            {'name': 'Personal Care', 'img': 'https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400'}
        ]
    },
    'books': {
        'name': 'Books & Media', 
        'img': 'https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=400',
        'sub_items': [
            {'name': 'Fiction', 'img': 'https://images.unsplash.com/photo-1474932430478-3a7fb9082db4?w=400'},
            {'name': 'Magazines', 'img': 'https://images.unsplash.com/photo-1504222490345-c075b6008014?w=400'},
            {'name': 'Art & Design', 'img': 'https://images.unsplash.com/photo-1513364776144-60967b0f800f?w=400'},
            {'name': 'Educational', 'img': 'https://images.unsplash.com/photo-1503676260728-1c00da07bb5e?w=400'},
            {'name': 'Comics', 'img': 'https://images.unsplash.com/photo-1541963463532-d68292c34b19?w=400'}
        ]
    },
    'auto': {
        'name': 'Automotive', 
        'img': 'https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400',
        'sub_items': [
            {'name': 'Car Accessories', 'img': 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?w=400'},
            {'name': 'Tools & Equipment', 'img': 'https://images.unsplash.com/photo-1530124560676-4fbc912f2796?w=400'},
            {'name': 'Auto Electronics', 'img': 'https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=400'},
            {'name': 'Oils & Fluids', 'img': 'https://images.unsplash.com/photo-1558981403-c5f91cbba527?w=400'},
            {'name': 'Safety', 'img': 'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=400'}
        ]
    },
    'pets': {
        'name': 'Pet Supplies', 
        'img': 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?w=400',
        'sub_items': [
            {'name': 'Pet Food', 'img': 'https://images.unsplash.com/photo-1589924691995-400dc9ca1144?w=400'},
            {'name': 'Grooming', 'img': 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?w=400'},
            {'name': 'Toys', 'img': 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?w=400'},
            {'name': 'Health', 'img': 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=400'},
            {'name': 'Beds', 'img': 'https://images.unsplash.com/photo-1541591419459-0c48ed20626c?w=400'}
        ]
    },
    'gifts': {
        'name': 'Gifts & Occasions', 
        'img': 'https://images.unsplash.com/photo-1513201099705-a9746e1e201f?w=400',
        'sub_items': [
            {'name': 'Personalized Gifts', 'img': 'https://images.unsplash.com/photo-1513201099705-a9746e1e201f?w=400'},
            {'name': 'Seasonal Gifts', 'img': 'https://images.unsplash.com/photo-1512331283953-19967202267a?w=400'},
            {'name': 'Greeting Cards', 'img': 'https://images.unsplash.com/photo-1534131707746-25d604851a1f?w=400'},
            {'name': 'Corporate Gifts', 'img': 'https://images.unsplash.com/photo-1511174511562-5f7f18b874f8?w=400'},
            {'name': 'Party Supplies', 'img': 'https://images.unsplash.com/photo-1530103043960-ef38714abb15?w=400'}
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', categories=CATEGORIES_DATA)

@app.route('/category/<cat_id>')
def category_page(cat_id):
    if cat_id in CATEGORIES_DATA:
        data = CATEGORIES_DATA[cat_id]
        return render_template('category.html', 
                               name=data['name'], 
                               sub_items=data['sub_items'],
                               categories=CATEGORIES_DATA)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
