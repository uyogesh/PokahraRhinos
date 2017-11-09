# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect,render_to_response
from django.views.generic import FormView,CreateView
from .forms import RegistrationForm
from .models import RegistrationFormModel
# Create your views here.

class RegForm(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    model = RegistrationFormModel
    success_url = 'registration/submit/'

    def form_valid(self, form):

          f_name = form['first_name']
          if form['middle_name'] is None:
              m_name = 'None'
          m_name = form['middle_name']
          l_name = form['last_name']
          dob = form['dob']
          citizenship_np = form['citizenship_no']
          poi = form['place_of_issue']
          mob_no = form['mobile_no']
          res_add = form['residential_add']
          email = form['email']
          sex = form['sex']
          height = form['height']
          weight = form['weight']
          played_for = form['played_for']
          bowling_arm = form['bowling_arm']
          bowling_pace = form['bowling_pace']
          wicket_keeper = form['wicket_keeper']
          club_name = form['club_name']
          batting = form['batting']
          first_preference = form['first_preference']
          team_captain_experience = form['team_captain_experience']
          health_issue = form['health_issues']
          other_details = form['other_details']

          model = RegistrationFormModel(f_name,
                                        m_name,
                                        l_name,
                                        dob,
                                        citizenship_np,
                                        poi,
                                        mob_no,
                                        res_add,
                                        email,
                                        sex,
                                        height,
                                        weight,
                                        played_for,
                                        bowling_arm,
                                        bowling_pace,
                                        wicket_keeper,
                                        club_name,
                                        batting,
                                        first_preference,
                                        team_captain_experience,
                                        health_issue,
                                        other_details)
          model.save()
          print f_name
          return super(RegForm, self).form_valid(form)





def Submit_form(request):

        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()

                return render(request,'success.html')
        else:
            form = RegistrationForm()

        return render(request,'registration.html', {'form': form})




  #
  #
  # def form_valid(self, form):
  #
  #       f_name = form['first_name']
  #       m_name = form['middle_name']
  #       l_name = form['last_name']
  #       dob = form['dob']
  #       citizenship_np = form['citizenship_no']
  #       poi = form['place_of_issue']
  #       mob_no = form['mobile_no']
  #       res_add = form['residential_add']
  #       email = form['email']
  #       sex = form['sex']
  #       height = form['height']
  #       weight = form['weight']
  #       played_for = form['played_for']
  #       bowling_arm = form['bowling_arm']
  #       bowling_pace = form['bowling_pace']
  #       wicket_keeper = form['wicket_keeper']
  #       club_name = form['club_name']
  #       batting = form['batting']
  #       first_preference = form['first_preference']
  #       team_captain_experience = form['team_captain_experience']
  #       health_issue = form['health_issues']
  #       other_details = form['other_details']
  #
  #       model = RegistrationFormModel(f_name,
  #                                     m_name,
  #                                     l_name,
  #                                     dob,
  #                                     citizenship_np,
  #                                     poi,
  #                                     mob_no,
  #                                     res_add,
  #                                     email,
  #                                     sex,
  #                                     height,
  #                                     weight,
  #                                     played_for,
  #                                     bowling_arm,
  #                                     bowling_pace,
  #                                     wicket_keeper,
  #                                     club_name,
  #                                     batting,
  #                                     first_preference,
  #                                     team_captain_experience,
  #                                     health_issue,
  #                                     other_details)
  #       model.save()
  #       print f_name
  #       return super(RegForm, self).form_valid(form)