## nysgerrig
* nysgerrig
  - utter_hvad_kan_jeg

## happy path
* hilsen
  - utter_hilsen
  - utter_bed_om_humør
* humør_glad
  - utter_glad

## sadhappy path
* hilsen
  - utter_hilsen
  - utter_bed_om_humør
* humør_trist
  - utter_opmuntring
  - utter_hjalp_det
* bekræft
  - utter_glad

## sad path 2
* hilsen
  - utter_hilsen
  - utter_bed_om_humør
* humør_trist
  - utter_opmuntring
  - utter_hjalp_det
* nægte
  - utter_er_der_andet

## say farvel
* farvel
  - utter_farvel
  - action_restart

## usikker
* hilsen
  - utter_hilsen
  - utter_bed_om_humør
* humør_trist
  - utter_opmuntring
  - utter_hjalp_det
* usikker
  - utter_er_der_andet

## interactive_story_1
* hilsen
    - utter_hilsen
* nysgerrig
    - utter_hvad_kan_jeg
* humør_trist
    - utter_opmuntring
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet

##FAQ kontaktinfo
* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* kontaktinformation
    - utter_kontaktinformation
* taknemmelig
    - utter_er_der_andet
* nægte
    - utter_farvel
    - action_restart

## unhappy indexsøgning
* indexsøgning
    - action_search_ent
    - utter_hjalp_det
* nægte
	- action_search_ent
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet

## happy index

* hilsen
    - utter_hilsen
* indexsøgning{"index":"indstillinger"}
    - action_search_ent
    - utter_hjalp_det
* bekræft
    - utter_er_der_andet
* nægte
	- utter_glad
    - utter_farvel
    - action_restart

## happy path søgning
* søgning
    - søgning_form
    - form{"name": "søgning_form"}
    - form{"name": null}
    - utter_hjalp_det
* bekræft
    - utter_er_der_andet
* nægte
	- utter_glad
    - utter_farvel
    - action_restart

## interactive_story_1
* kontaktinformation
    - utter_kontaktinformation
    - utter_er_der_andet
* nægte
    - utter_farvel
    - action_restart

## interactive_story_1
* hilsen
    - utter_hilsen
* humør_trist
    - utter_opmuntring
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet
* kontaktinformation
    - utter_kontaktinformation
    - utter_er_der_andet
* nægte
    - utter_farvel
    - action_restart

## Ingenting

* hilsen
    - utter_hilsen
* humør_glad
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* intet
    - utter_i_orden
    - utter_farvel
    - action_restart

## happy kontaktinfo

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* kontaktinformation
    - utter_kontaktinformation
    - utter_er_der_andet
* nægte
    - utter_i_orden
    - utter_farvel
    - action_restart

## bed om email

* email
    - utter_email
* taknemmelig
    - utter_i_orden
    - utter_er_der_andet
* nægte
    - utter_glad
    - utter_farvel
    - action_restart

## happy email

* email
    - utter_email
* taknemmelig
	- utter_så_lidt
    - utter_er_der_andet

## hilsen/hvad kan jeg gøre

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* humør_glad
    - utter_glad
    - utter_hvad_kan_jeg_gøre

## multiple search
* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning{"index":"tquery"}
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte
	- utter_skuffet_prøv_andet
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* bekræft
	- utter_glad
    - utter_er_der_andet
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"Date / Time"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## hilsen/kontakt/intetandet

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* kontaktinformation
    - utter_kontaktinformation
    - utter_er_der_andet
* nægte
    - utter_glad
    - utter_farvel
	- action_restart

## Tilbagevending efter hjælp

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* humør_trist
    - utter_opmuntring
    - utter_hjalp_det
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* kontaktinformation
    - utter_kontaktinformation
    - utter_er_der_andet
* nægte
    - utter_glad
    - utter_farvel
* iligemåde
    - utter_tak
* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* intet
    - utter_farvel
    - action_restart

## hej/email

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* email
    - utter_email
* taknemmelig
    - utter_er_der_andet
* nægte
    - utter_glad
    - utter_farvel
    - action_restart

## email farvel

* email
    - utter_email
* farvel
    - utter_farvel
    - action_restart

## tlf/email/tak/farvel

* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* email
    - utter_email
    - utter_er_der_andet
* taknemmelig
    - utter_i_orden
    - utter_er_der_andet
* nægte
	- utter_glad
    - utter_farvel
    - action_restart

## get_started

* get_started
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre

## hilsen/nummer/ja+addresse/tak/nejtak
* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* bekræft+addresse
    - utter_addr
    - utter_er_der_andet
* taknemmelig
    - utter_i_orden
    - utter_er_der_andet
* nægte
    - utter_farvel
    - action_restart

## addresse

* hilsen+addresse
	- utter_hilsen
    - utter_addr

## addresse tak

* hilsen+addresse
	- utter_hilsen
    - utter_addr
    - utter_er_der_andet
* taknemmelig
    - utter_i_orden
    - utter_er_der_andet

## hilsen+addresse multiple intent

* hilsen+addresse
    - utter_hilsen
    - utter_addr
    - utter_er_der_andet

## hilsen+søgning multiple intent
* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - action_search_ent
    - utter_hjalp_det

## interactive_story_1
* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name": "s\u00f8gning_form"}
    - slot{"requested_slot": "searchterm"}
* form: søgning
    - form: søgning_form
    - slot{"searchterm": "kage"}
    - slot{"searchterm": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_hjalp_det

## interactive_story_2
* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name": "s\u00f8gning_form"}
    - slot{"requested_slot": "searchterm"}
* form: null
    - form: søgning_form
    - slot{"searchterm": "tmenu"}
    - slot{"searchterm": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_hjalp_det
* taknemmelig
    - utter_er_der_andet

## Story from conversation with bc997c2290dd41eabe472c4bb8171d65 on September 18th 2019

* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* form: null
    - form: søgning_form
    - slot{"searchterm": "tmenu"}
    - slot{"searchterm": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_hjalp_det
* nægte+søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
    - utter_hjalp_det

## interactive_story_1
* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name": "s\u00f8gning_form"}
    - slot{"requested_slot": "searchterm"}
    - utter_hjalp_det

## Story from conversation with d33601cc12d1420c964fc124528da0c1 on September 18th 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* bekræft

## Story from conversation with 78c06b0824984d31a9171eb243d1b709 on September 18th 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* hilsen+søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - action_search_ent
    - utter_hjalp_det
* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - action_search_ent
    - utter_hjalp_det

## hilsen+søgning multiple intent
* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - action_search_ent
    - utter_hjalp_det
* nægte
	- utter_skuffet_prøv_andet
* bekræft+søg
	- søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}

## trist Tilbagevending efter hjælp

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* humør_trist
    - utter_opmuntring
    - utter_hjalp_det
* nægte
    - utter_trist
    - utter_hvad_kan_jeg_gøre
* kontaktinformation
    - utter_kontaktinformation
    - utter_er_der_andet
* nægte
    - utter_glad
    - utter_farvel
* iligemåde
    - utter_tak
* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* intet
    - utter_farvel
    - action_restart

## Story from conversation with e87c45aad52940c49201adeb858b779a on September 23rd 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* intet
    - utter_farvel
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* søgning
    - søgning_form
    - slot{"searchterm":"Kage"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte
    - utter_er_der_andet
* benægt+søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"Database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* bekræft
    - utter_er_der_andet
* nægte
    - utter_farvel
    - action_restart

## Story from conversation with e87c45aad52940c49201adeb858b779a on September 23rd 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* intet
    - utter_farvel
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* søgning
    - søgning_form
    - slot{"searchterm":"Kage"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet
* benægt+søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"Database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* bekræft
    - utter_er_der_andet
* nægte
    - utter_farvel
	- action_restart

## New Story

* hilsen+søgning
    - utter_hilsen
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet
* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* taknemmelig+nægte+farvel
    - utter_så_lidt
    - utter_farvel
    - action_restart

## New Story

* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* nægte+farvel
    - utter_i_orden
    - utter_farvel
    - action_restart

## New Story

* taknemmelig+nægte+farvel
    - utter_i_orden
    - utter_farvel
    - action_restart

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* addresse
    - utter_addr
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* addresse
    - utter_addr
    - utter_er_der_andet
* taknemmelig+nægte+farvel
    - utter_så_lidt
    - utter_farvel
    - action_restart

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* addresse
    - utter_addr
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* addresse
    - utter_addr
    - utter_er_der_andet
* bekræft+søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* bekræft
    - utter_er_der_andet
* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* nægte
    - utter_i_orden
    - utter_farvel
    - action_restart

## Story from conversation with 3413d81fede04eb4a74f2159221d9cf8 on September 25th 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* addresse
    - uttter_addr
    - utter_er_der_andet
* email
    - utter_email
* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* nægte
    - utter_glad
    - utter_farvel
    - action_restart

## Story from conversation with 15abc78bc5674497be68e4a2f667d8a9 on September 25th 2019

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* indexsøgning
    - action_search_ent
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* indexsøgning
    - action_search_ent
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* humør_glad
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* indexsøgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet

## Story from conversation with f13fb7bfd87b4e2fbdd828ede24ab221 on September 27th 2019

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* humør_glad
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* email
    - utter_email
* nægte+telefonnummer
    - utter_tlf

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* email
    - utter_email
    - utter_er_der_andet
* nægte+telefonnummer
    - utter_tlf
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* email
    - utter_email
* nægte+telefonnummer
    - utter_tlf

## Story from conversation with e034e4af8dc44c7b8951dda7a0e563e4 on September 27th 2019

* hilsen
    - utter_hilsen
* email
    - utter_email
* nægte+telefonnummer
    - utter_tlf
* nægte+telefonnummer
    - utter_tlf
    - utter_er_der_andet

## New Story

* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte+telefonnummer
    - utter_tlf
    - utter_er_der_andet
* taknemmelig+nægte+farvel
    - utter_i_orden
    - utter_farvel
    - action_restart

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* bekræft+email

## New Story

* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* bekræft+addresse
    - utter_addr

## New Story

* hilsen+addresse
    - utter_hilsen
    - utter_addr

## New Story

* hilsen+telefonnummer
    - utter_hilsen
    - utter_tlf
    - utter_er_der_andet

## New Story

* hilsen+email
    - utter_hilsen
    - utter_email
    - utter_er_der_andet

## Story from conversation with 29e86b6f839a49668d67cf3b8e6aae8d on September 30th 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* taknemmelig
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## Story from conversation with ab3aead0e3a34cb4badcb0bcf7eb9b18 on September 30th 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"eksporter"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* navn
	- utter_navn

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* navn
    - utter_navn
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"cookies"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* navn
    - utter_navn
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"cookies"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* navn
    - utter_navn
    - utter_hvad_kan_jeg_gøre

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* søgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* søgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* søgning
    - søgning_form
    - slot{"searchterm":"ostehøvl"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## Story from conversation with c3c414b6ddab4ab1b69c2b47fd59d841 on September 30th 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* navn
    - utter_navn
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* intet
    - søgning_form
    - form{"name":null}
    - slot{"requested_slot":null}
* email
    - utter_email
    - utter_er_der_andet
* telefonnummer
    - utter_tlf
    - utter_er_der_andet
* navn
    - utter_navn
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft+email
    - utter_glad
    - utter_email
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* nægte+email
    - utter_trist
    - utter_email
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft+telefonnummer
    - utter_glad
    - utter_tlf
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* nægte+telefonnummer
    - utter_trist
    - utter_tlf
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft+addresse
    - utter_glad
    - utter_addr
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* nægte+addresse
    - utter_trist
    - utter_addr
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* nægte+email
    - utter_email
    - utter_er_der_andet
* email
    - utter_email
    - utter_er_der_andet
* humør_trist
    - utter_opmuntring
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet
* bekræft+søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte+søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## Untitled Story
* iligemåde
	- utter_tak

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* nægte+søgning
    - utter_trist
    - søgning_form

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft+søgning
    - utter_glad
    - søgning_form

## Story from conversation with ef05fb62880e4afa9e73670c368aa4b9 on October 2nd 2019

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft
    - utter_glad
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* taknemmelig
    - utter_er_der_andet
* nægte
    - utter_glad
    - utter_farvel

## Story from conversation with a535137cc5d5403fb59878d8d149c729 on October 2nd 2019

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft+søgning
    - utter_glad
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"tquery"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* taknemmelig
    - utter_er_der_andet
* bekræft+email
    - utter_email
    - utter_er_der_andet

## Story from conversation with dccf74cc4dd94c40bc4251899bdd489f on October 3rd 2019

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* taknemmelig
    - utter_så_lidt
    - utter_er_der_andet

## Untitled Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* email
	- utter_email

## Untitled Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* addresse
	- utter_addr
    - utter_er_der_andet

## Untitled Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* telefonnummer
	- utter_tlf
    - utter_er_der_andet

## New Story

* hilsen
    - utter_hilsen

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"afbetaling"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
* nægte
    - utter_skuffet_prøv_andet
* bekræft
    - utter_hvad_kan_jeg_gøre
* intet
    - utter_farvel
    - action_restart

## Story from conversation with 477e025542ae45a6a45b7025199359af on October 4th 2019

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft+email
    - utter_glad
    - utter_email
    - utter_er_der_andet
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"kkk"}
    - slot{"searchterm":null}
    - form{"name":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"kage"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_bed_om_humør
* bekræft+email
    - utter_glad
    - utter_email
    - utter_er_der_andet
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"kkk"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"kkk"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* indexsøgning
    - søgning_form
    - slot{"searchterm":"database"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"kage"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det

## New Story

* hilsen
    - utter_hilsen
    - utter_hvad_kan_jeg_gøre
* søgning
    - søgning_form
    - form{"name":"søgning_form"}
    - slot{"requested_slot":"searchterm"}
* null
    - søgning_form
    - slot{"searchterm":"kage"}
    - slot{"searchterm":null}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_hjalp_det
