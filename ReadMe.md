# RASP

## Boş yazılım planlaması
Bu planlamaları burada yapmak ne kadar mantıklı bilmiyorum. Neyse

Menüler için bir tane metaclass şimdilik MetaMenu diyelim, BaseMenu diye baba menümüz olur (diğer menülerin classlarını inheritlemek için) ondan bir iki template türetiriz, her menü class olacak, classlar static (@classmethod) dolu olacak o yüden menü objeleri üretilmeyecek. Templatelerden türeyen MainMenu diğer akrabalrını çağırmakta sıkıntı çekmeyecek (yüşanın telefon rehberidenki gibi olmayacak). 

Kaydırma vs işlemleri yakalaması için handler dosyası olur (lib içinde) menuler yakalama işlemlerini oradan yapar.

Menülerde direkt print ya da pygame.write tarzında bir şey yapma, yazılar için write çağır, pygame üzerinde kullanacaksam wrapper yazarım

<br>

### File Explorer, Airdump-ng, metaploit, nmap, whatsapp, ve ssh desteği kesinlikle gerekiyor. Hepsi için ayrı 3. parti package kullanırım.
<br>

Saat gösteren menünün arayüzü önemli belki birden fazla tema seçeneği olabilir, belki bir iki küçük oyun ekleyebilirim, (snake, pong ya da shadow casting gibi projeler de olabilir) **pygame_gui** kullanımına bakmam lazım, **datetime** öğrenmem lazım.

Arayüz için temalardan bir tanesi [MEGABOI](https://github.com/tunapro1234/MEGABOI) tarzı arayüz olmak zorunda.

**log** sistemi güzel olabilirdi

<br>

Şimdi küçük bir mesele var, temalar class objesi olarak tutulabilir ama draw fonksiyonları tema için bir parametre almaları gerekiyor, (tem a  preview olayları için) 