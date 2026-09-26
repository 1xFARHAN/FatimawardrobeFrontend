import { createContext, useContext, useEffect, useState } from 'react';

export type BagItem = { id: string; size: string; quantity: number };

type StoreValue = {
  wishlist: string[];
  bag: BagItem[];
  bagOpen: boolean;
  toggleWish: (id: string) => void;
  addToBag: (id: string, size: string, quantity?: number) => void;
  removeFromBag: (id: string, size: string) => void;
  changeQuantity: (id: string, size: string, by: number) => void;
  clearBag: () => void;
  openBag: () => void;
  closeBag: () => void;
};

const StoreContext = createContext<StoreValue | null>(null);

function readStore<T>(key: string, fallback: T): T {
  if (typeof window === 'undefined') return fallback;
  try {
    const stored = window.localStorage.getItem(key);
    return stored ? JSON.parse(stored) as T : fallback;
  } catch {
    return fallback;
  }
}

export function StoreProvider({ children }: { children: React.ReactNode }) {
  const [wishlist, setWishlist] = useState<string[]>([]);
  const [bag, setBag] = useState<BagItem[]>([]);
  const [bagOpen, setBagOpen] = useState(false);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setWishlist(readStore('fatima-wishlist', []));
    setBag(readStore('fatima-bag', []));
    setHydrated(true);
  }, []);

  useEffect(() => {
    if (!hydrated) return;
    window.localStorage.setItem('fatima-wishlist', JSON.stringify(wishlist));
    window.localStorage.setItem('fatima-bag', JSON.stringify(bag));
  }, [bag, hydrated, wishlist]);

  const toggleWish = (id: string) => {
    setWishlist((old) => old.includes(id) ? old.filter((item) => item !== id) : [...old, id]);
  };

  const addToBag = (id: string, size: string, quantity = 1) => {
    setBag((old) => {
      const found = old.find((item) => item.id === id && item.size === size);
      if (found) return old.map((item) => item === found ? { ...item, quantity: item.quantity + quantity } : item);
      return [...old, { id, size, quantity }];
    });
  };

  const removeFromBag = (id: string, size: string) => {
    setBag((old) => old.filter((item) => !(item.id === id && item.size === size)));
  };

  const changeQuantity = (id: string, size: string, by: number) => {
    setBag((old) => old.flatMap((item) => {
      if (item.id !== id || item.size !== size) return [item];
      const quantity = item.quantity + by;
      return quantity > 0 ? [{ ...item, quantity }] : [];
    }));
  };

  const value: StoreValue = {
    wishlist,
    bag,
    bagOpen,
    toggleWish,
    addToBag,
    removeFromBag,
    changeQuantity,
    clearBag: () => setBag([]),
    openBag: () => setBagOpen(true),
    closeBag: () => setBagOpen(false),
  };

  return <StoreContext.Provider value={value}>{children}</StoreContext.Provider>;
}

export function useStore() {
  const store = useContext(StoreContext);
  if (!store) throw new Error('useStore must be used inside StoreProvider');
  return store;
}